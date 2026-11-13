---
declaration: section
origin: cited
lean: MetaMathlibExt.terai_ten_fifteen_five_eq_one_one_two, MetaMathlibExt.gaussClassNumber_neg_four_mul_lt
statement: formalized
---

# Terai's conjecture

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/terai-s-conjecture/index.html).

## The Terai equation $(10m^2 + 1)^x + (15m^2 - 1)^y = (5m)^z$

For every integer
$m > 1$, the only solution of $(10m^2 + 1)^x + (15m^2 - 1)^y = (5m)^z$ in positive integers
$x, y, z$ is $(x, y, z) = (1, 1, 2)$.

## Sources

- Kalyan Chakraborty and Meenu Sharma, *A Note on Terai's Conjecture Related to Exponential Diophantine Equations*, INTEGERS 26 (2026), Article A67, Theorem 2.

Stated but not proved: `MetaMathlibExt.terai_ten_fifteen_five_eq_one_one_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/TeraiTypeExponentialEquationWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TeraiTypeExponentialEquationWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/terai-s-conjecture/index.html#terai-ten-fifteen-five-eq-one-one-two).

## Hua's class number bound

For every positive integer $D$, the Gauss class number
$h(-4D)$, the number of primitive, reduced, positive definite binary quadratic forms of
discriminant $-4D$, satisfies $h(-4D) < \frac{4}{\pi} \sqrt{D} \log(2e\sqrt{D})$, where $\log$ is
the natural logarithm.

The source quotes this bound from Hua's textbook for the class number of positive binary
quadratic forms; it is read here as the primitive (Gauss) class number.

## Sources

- Kalyan Chakraborty and Meenu Sharma, *A Note on Terai's Conjecture Related to Exponential Diophantine Equations*, INTEGERS 26 (2026), Article A67, Theorem 3.

Stated but not proved: `MetaMathlibExt.gaussClassNumber_neg_four_mul_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/TeraiTypeExponentialEquationWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TeraiTypeExponentialEquationWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/terai-s-conjecture/index.html#gauss-class-number-neg-four-mul-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Terai's conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/terai-s-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/terai-s-conjecture)
