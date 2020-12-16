#ifndef _SHAPE_H_
#define _SHAPE_H_
#include "centrallib.h"
#include "utils.h"

using namespace std;

class Shape
{
    private:
        float width = 0;
        float height = 0;
        std::string drawType = "*";

    public:
        Shape() {}
        Shape(float _width = 0, float _height = 0, std::string _drawType = "*")
        {
            if(width < 0 || height <= 0)
            {
                std::cerr << "Width and height is not valid" << std::endl;
            }
            else{
                width = _width;
                height = _height;
                drawType = _drawType;
            }
        }
    
    public:
        static Shape parseInfoFromInput(vector<string> input)
        {
            Shape shape = new Shape();
            switch (to_lower(input[0]))
            {
            case "equilateral" :
                /* code */
                break;
            case "isosceles" :
                break;
            case "right_angled" :
                break;
            case "scalene" :
                break;  
            case "square" :
                break;
            case "rectangles" :
                break;
            case "elipse" :
                break;              
            default:
                break;
            }
        }

    public:
        virtual void draw() {}

}

#endif