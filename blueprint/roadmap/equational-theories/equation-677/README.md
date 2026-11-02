# Equation 677

In this chapter we study finite magmas that satisfy equation 677,

$$
x = y \diamond (x \diamond ((y \diamond x) \diamond y))
$$

for all $x,y$, and whether this implies equation 255,

$$
x = ((x \diamond x) \diamond x) \diamond x.
$$

Using the usual notation $L_y x = y \diamond x$, $R_y x = x \diamond y$, $Sx = x \diamond x$, we can rewrite equation 677 as

$$
x = L_y L_x L_{L_y x} y = L_y (x \diamond R_y L_y x)
$$

and 255 as

$$
x = (Sx \diamond x) \diamond x.
$$

- [Basic properties of 677 magma](677-basic.md)
- [255-equiv](255-equiv.md)
- [No linear counterexamples](linear-obstruction.md)
- [No counterexamples via linear extension](linear-2.md)
- [The free 677 magma](the-free-677-magma/README.md)
