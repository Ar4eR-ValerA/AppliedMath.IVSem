#ifndef BASEFUNC_H
#define BASEFUNC_H

class IFunc {
public:
    virtual double GetResult(double x) const = 0;
};

#endif //BASEFUNC_H