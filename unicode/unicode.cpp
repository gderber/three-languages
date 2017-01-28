/*******************************************************************************
 *
 * Unicode.cpp
 *
 ******************************************************************************/

/*******************************************************************************
 *
 * Std libraries:
 * iostream
 *
 * Other Libraries:
 * tclap
 *
 *
 * Application Libraries:
 * colors.hh - provides for color text
 *
 ******************************************************************************/
//Standard Libraries
#include <iostream>
#include <string>
#include <iomanip>

//Other Libraries
#include <tclap/CmdLine.h>

//Application Libraries
#include "../lib/cpp/colors.hh"

/****
 *
 * Preprossesor Definitions
 *
 *****/
std::string VERSION = "0.1.1";

/***************************
 *
 * function colortext::set_color
 *
 ********/
void colortext::set_color (std::string t, std::string a, std::string fg, std::string bg) {
  textstring = t;
  attribute = a;
  fgcolor = fg;
  bgcolor = bg;
}

std::string intToHexString(int intValue) {

  /// integer value to hex-string
  std::stringstream sstream;
  sstream << "0x"
	  << std::setfill ('0') << std::setw(4)
	  << std::hex << (int)intValue;

  return sstream.str();
}

int main(int argv, char *argc[]) {

  /*
  try {
    TCLAP::CmdLine cmd("Command description message", ' ', VERSION);
    TCLAP::ValueArg<std::string> nameArg("n",
					 "name",
					 "Name to print",
					 true,
					 "homer",
					 "string");
    cmd.add(nameArg);
  */

  for (int x = 0; x < 65535;x++) {
    std::string unistring = intToHexString(x);
    std::cout << unistring << '\n';
    wchar_t unichar = unistring;
    std::wcout << unichar << '\n';
  }
      

  colortext colorstring;
  colorstring.set_color ("Hello World!","none","red","black");
  std::cout << colorstring.colorize() << '\n';
  colorstring.set_color ("What's Up Doc?","none","blue","black");
  std::cout << colorstring.colorize() << '\n';

  return 0;
}
