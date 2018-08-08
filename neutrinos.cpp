#include <iostream>

class Brain
{
    public:
    char name[];
};
class Alpha
{ 
    Brain brains[];
    Alpha private_Alphas[];
    Beta private_Betas[];
    protected:
    Alpha protected_Alphas;
    Beta protected_Betas;
    public:
    char name[];
    Alpha public_Alphas[];
    Alpha(int name_len,char Name[name_len])
    {
        for (int i = 0;i <name_len; i++)
        name[name_len] = Name[name_len];
    }
};

class Beta
{
    public:
    char name[];
};
