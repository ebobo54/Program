Version: 1.0

[The original library is cross-compatible. This one has minor changes so should be as well. However I only tested in Linux.]

I hosted this since I found N. Devillard's gnuplot_i for C of great use. 

Unlike other gnuplot_i derived projects, this one is a slim bundle of the C interface and a C++ wrapper. 

I patched N. Devillard's library to allow compatibility with C and C++ directly. 
I also added a separate C++ wrapper through a class which sticks to the original API. 

Both C and C++ interfaces remain available and no junk is added to neither.

The advantages with the C++ wrapper are: 

    - Automated initialization and closing procedures through RAII.
    - Same performance
    - Same calling convention
    - Less verbosity 



The codebase is based on N. Devillard's 2.10 revision.


############################
USAGE:
############################

C project:
1 - "make c"
2 - Compile your program with the object gnuplot_i.o  (gcc -o my_program my_program_code.c gnuplot_i.o)

C++ project:
1 - "make cpp"
2 - Compile your program with the object gnuplot_ipp.o  (gcc -o my_program my_program_code.c gnuplot_ipp.o)


############################
Documentation:
############################

gnuplot_i homepage: http://ndevilla.free.fr/gnuplot/

gnuplot_i documentation: http://ndevilla.free.fr/gnuplot/gnuplot_i/ 

gnuplot_i API: http://ndevilla.free.fr/gnuplot/gnuplot_i/gnuplot__i_8h.html

No documentation is needed for the C++ wrapper. Just read the gnuplot_i API and gnuplot_ipp.h ;)


