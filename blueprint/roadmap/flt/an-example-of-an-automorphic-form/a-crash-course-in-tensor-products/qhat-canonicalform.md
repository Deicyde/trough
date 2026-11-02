---
declaration: lemma
origin: cited
lean: QHat.canonicalForm
statement: formalized
proof: formalized
---

# QHat.canonicalForm

Every element of $\widehat{\mathbb{Q}}:=\mathbb{Q}\otimes\widehat{\mathbb{Z}}$ can be written as $q\otimes_t z$ with $q\in\mathbb{Q}$ and $z\in\widehat{\mathbb{Z}}$. Furthermore one can even assume that $q=\frac{1}{N}$ for some positive integer $N$.

## Depends on

- [QHat](../qhat-and-tensor-products/qhat.md)
- [ZHat.commRing](../zhat/zhat-commring.md)

## Proof

A proof I would write on the board would look like the following. Take a general element of $\widehat{\mathbb{Q}}$; we know it can be expressed as a finite sum $\sum_i q_i\otimes_t z_i$ with $q_i\in\mathbb{Q}$ and $z_i\in\widehat{\mathbb{Z}}$. Now choose a large positive integer $N$, the lowest common multiple of all the denominators showing up in the $q_i$, and then rewrite $\sum_i q_i\otimes_t z_i$ as $\sum_i \frac{n_i}{N}\otimes z_i$ with $n_i\in\mathbb{Z}$. Now using the fundamental fact that $na\otimes_t b=a\otimes_t nb$ for $n\in\mathbb{Z}$, we can rewrite the sum as $\sum_i \frac{1}{N}\otimes_t n_i z_i$ which is equal to the pure tensor $\frac{1}{N}\otimes(\sum_i n_i z_i)$.

In Lean I would prove this using TensorProduct.induction\_on, which quickly reduces us to the claim that the sum of two pure tensors is pure, which we can prove using the above technique whilst avoiding the general theory of finite sums.

## Lean

Formalized as [`QHat.canonicalForm`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QHat.canonicalForm).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 332](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L332)
