---
declaration: lemma
origin: cited
lean: I₃_eq, sum_condMutual_le
statement: formalized
proof: formalized
---

# Bound on conditional mutual informations

We have

$$
I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) \leq 6 \eta k - \frac{1 - 5 \eta}{1-\eta} (2 \eta k - I_1).
$$

## Depends on

- [Conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-def.md)

## Proof depends on

- [Second estimate](../second-estimate/second-estimate.md)
- [Symmetry identity](symm-lemma.md)

## Proof

From the definitions of $I_1,I_2$ and [Symmetry identity](symm-lemma.md), we see that

$$
I_1 = I(U : V \, | \, S), \qquad I_2 = I(W : U \, | \, S), \qquad I_2 = I(V : W \, | \,S).
$$

Applying [First estimate](../first-estimate/first-estimate.md) and [Second estimate](../second-estimate/second-estimate.md) we have the inequalities

$$
I_2 \leq 2 \eta k + \frac{2\eta(2 \eta k - I_1)}{1-\eta} .
$$

We conclude that

$$
I_1 + I_2 + I_2 \leq I_1+4\eta k+ \frac{4\eta(2 \eta k - I_1)}{1-\eta}
$$

and the claim follows from some calculation.

## Lean

Formalized as [`I₃_eq`](https://teorth.github.io/pfr/docs/find/#doc/I₃_eq), [`sum_condMutual_le`](https://teorth.github.io/pfr/docs/find/#doc/sum_condMutual_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 255](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L255)
