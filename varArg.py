def varArg( arg1, *multiArg ):
    print("The first argument is : ",arg1 )
    for param in multiArg:
        print("The next arguments is : ",param)

    return

varArg(10)
varArg(10,20,30,40,50)