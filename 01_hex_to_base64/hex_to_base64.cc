std::string HexStr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";

#include "iostream"
#include "openssl/bio.h"
#include "openssl/evp.h"
#include "openssl/buffer.h"

std::string decode_hex_string (const std::string &);
std::string encode_base64 (const std::string &);

int main ()
{

  std::string res = encode_base64( decode_hex_string (HexStr) );

  std::cout << res << "\n";
  assert ( "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n" == res );
}

std::string decode_hex_string (const std::string & hex_string)
{
  std::string res;
  int i = 0;
  while (i < hex_string.length())
  {
    std::string hex_digit = hex_string.substr( i, 2 );
    long long ascii = std::strtol( hex_digit.c_str(), nullptr, 16 );
    res += (char) ascii;
    i += 2;
  }
  std::cout << "/decode_hex_string: " << res << "\n";
  return res;
}

std::string encode_base64 (const std::string & input) {

  BIO       *bio, *b64;
  BUF_MEM   *bufferPtr;

  b64 = BIO_new(BIO_f_base64());
  bio = BIO_new(BIO_s_mem());
  bio = BIO_push(b64, bio);

  BIO_write(bio, input.c_str(), input.length());
  BIO_flush(bio);
  BIO_get_mem_ptr(bio, &bufferPtr);

  std::string encoded(bufferPtr->data, bufferPtr->length);
  BIO_free_all(bio);

  std::cout << "/encoded base64: " << encoded << "\n";

  return encoded;
}


