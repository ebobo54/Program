// gnuplot_ipp 1.0

/*
  LICENSE

  Author: Alberto E. A. Ferreira
  Date: Feb/2014

  Use for any purpose you want as long as you cite.
  Feel free to ask stuff: features / questions.
*/

/*
  DESCRIPTION

  This is simply a wrapper to N. Devillard's code. 
   It requires the bundled modified C files to work.

  To learn how to use it read the documentation of the original 
    C library as this interface directly wraps such functions.
*/

#ifndef GNUPLOT_IPP_H__
#define GNUPLOT_IPP_H__

#include "gnuplot_i.h"


/// Plot class (wraps the C interface identically) Also allows returning the handle
class Gnuplot
{
public:
	Gnuplot()  { h = gnuplot_init ( ); }
	~Gnuplot() {     gnuplot_close(h); }

	// Useful for direct manipulation if new commands on the base library are not wrapped yet
	gnuplot_ctrl * get_handle() { return h; } 

	void set_xlabel(const char *label) { gnuplot_set_xlabel(h,label); }
	void set_ylabel(const char *label) { gnuplot_set_ylabel(h,label); }
	void set_labels(const char *label_x, const char *label_y) { gnuplot_set_xlabel(h,label_x); gnuplot_set_ylabel(h,label_y); }

	void setstyle(const char *style) { gnuplot_setstyle(h,style); }

	void plot_x   (double *y, int n, const char *title) { gnuplot_plot_x(h,y,n,title); }
	void plot_xy  (double *x, double *y, int n, const char *title) { gnuplot_plot_xy(h,x,y,n,title);}

	void replot_x (double *y, int n, const char *title) { reset(); plot_x(y,n,title); }
	void replot_xy(double *x, double *y, int n, const char *title) { reset(); plot_xy(x,y,n,title); }
	
	void plot_once     (const char *title, const char *style, const char *label_x, const char *label_y, double *x, double *y, int n) { gnuplot_plot_once (title, style, label_x, label_y, x, y, n); }
	void plot_slope    (double a, double b, const char *title) { gnuplot_plot_slope (h, a, b, title); }
	void plot_equation (const char *equation, const char *title) { gnuplot_plot_equation (h, equation, title); }

	void reset() { gnuplot_resetplot(h); }

	void cmd(char const *  cmd, ...); 

private:
	gnuplot_ctrl *h;
};


void Gnuplot::cmd(char const *cmd, ...)
{
	va_list args; 
	va_start(args, cmd);

	gnuplot_vcmd(h, cmd, args);

	va_end(args);
}


#endif // GNUPLOT_IPP_H__
