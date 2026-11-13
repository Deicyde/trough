---
declaration: section
origin: cited
lean: MetaMathlibExt.jacobsthalLucasNumber, MetaMathlibExt.jacobsthal_closedForm
statement: formalized
proof: formalized
---

# Jacobsthal and Jacobsthal–Lucas numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/jacobsthal-and-jacobsthal-lucas-numbers/index.html).

## Jacobsthal–Lucas numbers

The Jacobsthal–Lucas numbers $j_0, j_1, j_2, \dots$ are the
natural numbers defined by $j_0 = 2$, $j_1 = 1$ and $j_{n+2} = j_{n+1} + 2 j_n$ for all
$n \ge 0$. The sequence begins $2, 1, 5, 7, 17, \dots$ (OEIS A014551).

Formalized by `MetaMathlibExt.jacobsthalLucasNumber`, a definition declared in [MathlibExt/NumberTheory/JacobsthalLucasNumber.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/JacobsthalLucasNumber.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/jacobsthal-and-jacobsthal-lucas-numbers/index.html#jacobsthal-lucas-number).

## Jacobsthal closed form

Let $J : \mathbb{N} \to \mathbb{N}$ satisfy $J(0) = J(1) = 1$ and
$J(n+2) = J(n+1) + 2J(n)$ for every $n \in \mathbb{N}$. Then for every $m \in \mathbb{N}$,

$$J(m) = \frac{2^{m+1} + (-1)^m}{3}.$$

The source cites A. Tucker, "Applied Combinatorics," 3rd edition, for this formula. The proof
applies Binet's formula for second-order linear recurrences; the characteristic polynomial
$x^2 - x - 2$ has roots $2$ and $-1$.

## Sources

- Darrin D. Frey and James A. Sellers, "Jacobsthal Numbers and Alternating Sign Matrices," Journal of Integer Sequences 3 (2000), Article 00.2.3, recurrence with initial values, lines 260–266, and Theorem, equation (Eq4a), lines 329–335, https://cs.uwaterloo.ca/journals/JIS/VOL3/SELLERS/sellers.tex

Formalized by `MetaMathlibExt.jacobsthal_closedForm`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/JacobsthalClosedForm.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/JacobsthalClosedForm.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/jacobsthal-and-jacobsthal-lucas-numbers/index.html#jacobsthal-closed-form).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobsthal and Jacobsthal–Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/jacobsthal-and-jacobsthal-lucas-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/jacobsthal-and-jacobsthal-lucas-numbers)
