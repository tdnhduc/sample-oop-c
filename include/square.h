#include "centrallib.h"
#include "shape.h"

class Square : public Shape
{
    public:
        void draw()
        {
            cout << "Draw square" << endl;
        }
};
