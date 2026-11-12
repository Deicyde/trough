---
declaration: section
origin: cited
lean: OAI.QuarticPowerFree.allDegrees
statement: formalized
proof: formalized
---

# 020. Squarefree quartics and power-free polynomial values

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the squarefree-values conjecture for irreducible integer quartics with no fixed prime-square divisor: squarefree values on positive integers have the predicted positive Euler-product density. More generally, establishes the $(d-2)$-power-free density for irreducible integer polynomials of degrees four through eight under the necessary local condition; together with Browning's higher-degree theorem, this covers every *d* ≥ 4.

## Squarefree values of quartics and power-free values of polynomials

We prove that every irreducible integer quartic with no fixed prime-square divisor takes squarefree values with the predicted positive Euler-product density. More generally, we obtain the corresponding $(d-2)$-power-free density in degrees $4\le d\le8$. The proof combines number-field factorization, determinant estimates with adaptive auxiliary primes, and explicit low-degree geometry. Together with Browning's theorem for higher degrees, this gives the $(d-2)$-power-free density for every *d* ≥ 4.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves positive-density power-free values for every integer polynomial $f$ irreducible over $\mathbb Q$ of degree $d\ge4$. Put $k=d-2$ and assume no prime $k$th power divides every value of $f$. Then the number of positive integers $n\le X$ for which $f(n)$ is $k$-free is $c_fX+o_f(X)$, where $c_f>0$ is the convergent product of local factors. Negative values are allowed and zero is excluded. No monicity, primitivity, or coefficient-height restriction is imposed.

## Lean: Positive density of power-free polynomial values

Stated in [PowerFreeValues.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PowerFreeValues.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem allDegrees (f : Polynomial ℤ)
    (hirr : Irreducible (f.map (Int.castRingHom ℚ)))
    (hdeglo : 4 ≤ f.natDegree)
    (hlocal : LocallyAdmissible f (f.natDegree - 2)) :
    DensityStatement f (f.natDegree - 2)
```

Proved in [lean/OAI/NumberTheory/PowerFree/Main.lean, line 144](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/PowerFree/Main.lean#L144).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/020.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/020.md)
