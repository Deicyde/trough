# Cohn-Elkies linear programming bounds

In 2003 Cohn and Elkies (ElkiesCohn) developed linear programming bounds that apply directly to sphere packings. The goal of this section is to formalize the Cohn–Elkies linear programming bound.

The following theorem is the key result of (ElkiesCohn). (Note that the original theorem is stated for a class of functions more general then Schwartz functions.)

- [Cohn–Elkies (ElkiesCohn)](thm-cohn-elkies-periodic.md)
- [Cohn–Elkies (ElkiesCohn)](thm-cohn-elkies-general.md)

The main step in our proof of [Corollary MainTheorem](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/main-result.tex#L20) is the explicit construction of an optimal function. It will be convenient for us to scale this function by $\sqrt{2}$.

Theorem [Cohn–Elkies (ElkiesCohn)](thm-cohn-elkies-general.md) applied to the optimal function $f(x)=g(x/\sqrt{2})$ immediately implies [Corollary MainTheorem](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/main-result.tex#L20).
