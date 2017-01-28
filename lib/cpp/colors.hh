/*******************************************************************************
 *
 * colors.hh
 *
 ******************************************************************************/
#include <iostream>
#include <string>

class colortext {
private:
  std::string textstring, attribute, fgcolor, bgcolor;
public:
  void set_color (std::string, std::string, std::string, std::string);
  std::string colorize () {
    const std::string escape = "\x1b[";

    std::string strattribute,strfgcolor,strbgcolor;

    //List of attributes
    if (attribute == "bold") {
      strattribute = "1";
    }
    else if (attribute == "unk_a") {
      strattribute = "2";
    }
    else if(attribute == "unk_b") {
      strattribute = "3";
    }
    else if(attribute == "underline") {
      strattribute = "4";
    }
    else if(attribute == "blink") {
      strattribute = "5";
    }
    else if(attribute == "unk_c") {
      strattribute = "6";
    }
    else if(attribute == "reverse") {
      strattribute = "7";
    }
    else {
      strattribute = "0";
    }

    //Foreground colors
    if (fgcolor == "black") {
      strfgcolor = "30";
    }
    else if (fgcolor == "red") {
      strfgcolor = "31";
    }
    else if (fgcolor == "green") {
      strfgcolor = "32";
    }
    else if (fgcolor == "yellow") {
      strfgcolor = "33";
    }
    else if (fgcolor == "blue") {
      strfgcolor = "34";
    }
    else if (fgcolor == "fuchsia") {
      strfgcolor = "35";
    }
    else if (fgcolor == "magenta") {
      strfgcolor = "35";
    }
    else if (fgcolor == "turquoise") {
      strfgcolor = "36";
    }
    else if (fgcolor == "cyan") {
      strfgcolor = "36";
    }
    else {
      strfgcolor = "37";
    }

    //Background colors
    if (bgcolor ==  "red") {
      strbgcolor = "41";
    }
    else if (bgcolor ==  "green") {
      strbgcolor = "42";
    }
    else if (bgcolor ==  "yellow") {
      strbgcolor = "43";
    }
    else if (bgcolor ==  "blue") {
      strbgcolor = "44";
    }
    else if (bgcolor ==  "fuchsia") {
      strbgcolor = "45";
    }
    else if (bgcolor == "magenta") {
      strbgcolor = "45";
    }
    else if (bgcolor ==  "turquoise") {
      strbgcolor = "46";
    }
    else if (bgcolor ==  "cyan") {
      strbgcolor = "46";
    }
    else if (bgcolor ==  "white") {
      strbgcolor = "47";
    }
    else {
      strbgcolor = "40";
    }

    std::string newstring = escape + strattribute + ";" + strfgcolor + ";" + strbgcolor + "m" + textstring + escape + "0;30;40m";
    return newstring;
  }
};
