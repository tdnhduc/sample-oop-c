#include "centrallib.h"
#include "shape.h"

class Triangle : public Shape
{
    public:
        void draw()
        {
            cout << "draw triangle" << endl;
        }
};