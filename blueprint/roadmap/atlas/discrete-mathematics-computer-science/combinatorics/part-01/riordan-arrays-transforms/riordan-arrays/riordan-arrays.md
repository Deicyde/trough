---
declaration: section
origin: cited
lean: MetaMathlibExt.rFibonacciNumber, MetaMathlibExt.shiftedRiordanArray_constantTerm_and_sumCoefficients, MetaMathlibExt.diagonalSums, MetaMathlibExt.triple_factorization_of_dot_diagram, MetaMathlibExt.twin_powers
statement: formalized
proof: formalized
---

# Riordan arrays and number triangles: its own results

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html).

Riordan arrays and their A- and Z-sequences, inverses, triple factorizations, pseudo-involutions and total positivity, the Pascal and Pell matrices as Riordan arrays, Barry's triangles, triangular recurrence arrays extended to negative rows, and diagonal or row sums of triangles.

## Barry–Hennessy generalized Fibonacci numbers

For a real number $r$ and a natural number
$n$, the $r$-parameter generalized Fibonacci number is the real number

$$F_r(n) = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n-k}{k} r^k.$$

## Sources

- Paul Barry and Aoife Hennessy, *Notes on a Family of Riordan Arrays and Associated Integer Hankel Transforms*, Journal of Integer Sequences 12 (2009), Article 09.5.3.

Formalized by `MetaMathlibExt.rFibonacciNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RParameterGeneralizedFibonacciSequence.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RParameterGeneralizedFibonacciSequence.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html#r-fibonacci-number).

## Constant term and row sum of a shifted array

Let $R$ be a commutative semiring, let
$(A_{i,k})_{i,k \in \mathbb{N}}$ be an array with entries in $R$, and let $r \in R$ and
$n \in \mathbb{N}$. For $s \in R$ let $A^{(s)}$ be the $s$-shifted array with entries
$A^{(s)}_{i,j} = \sum_{k=j}^{i} \binom{k}{j} A_{i,k} s^{k-j}$ (an empty sum when $j > i$), and let
$p(X) = \sum_{k=0}^{n} A^{(r)}_{n,k} X^k \in R[X]$ be the $n$-th row polynomial of $A^{(r)}$.
Then $p(0) = A^{(r)}_{n,0} = \sum_{k=0}^{n} A_{n,k} r^k$ and
$p(1) = \sum_{k=0}^{n} A^{(r)}_{n,k} = A^{(r+1)}_{n,0}$.

## Sources

- José Agapito, Ângela Mestre, Maria M. Torres, and Pasquale Petrullo, "On One-Parameter Catalan Arrays," Journal of Integer Sequences 18 (2015), Article 15.5.1, Corollary (equations eqColumn0Rr and eqRowsumsRr), lines 240–245, https://cs.uwaterloo.ca/journals/JIS/VOL18/Agapito/agapito2.tex

Formalized by `MetaMathlibExt.shiftedRiordanArray_constantTerm_and_sumCoefficients`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/ShiftedRiordanArrayRowSums.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/ShiftedRiordanArrayRowSums.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html#shifted-riordan-array-constant-term-and).

## Diagonal sums of an array

For a doubly indexed array $(a_{i,j})_{i, j \ge 0}$ with entries
in an additive commutative monoid $M$, the $n$-th diagonal sum is
$d_n = \sum_{i + j = n} a_{i,j} = \sum_{k=0}^{n} a_{k,n-k}$.

If $a$ is a lower-triangular array with $a_{i,j}$ in row $i$ and column $j$, these are its sums
along rising diagonals. For a Riordan array $(g, f)$, whose column $j$ has generating function
$g(x) f(x)^j$, the sequence $(d_n)$ has generating function $g(x) / (1 - x f(x))$.

Formalized by `MetaMathlibExt.diagonalSums`, a definition declared in [MathlibExt/Combinatorics/Enumerative/DiagonalSumsOfARiordanOrTriangularArray.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DiagonalSumsOfARiordanOrTriangularArray.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html#diagonal-sums).

## Peart–Woodson triple factorization of Riordan arrays

Let $b$ be an integer, let
$\varepsilon$, $\delta$ and $\lambda$ be real numbers, and let $g$ and $f$ be formal power series
over $\mathbb{R}$ with $g(0) = 1$ and $f(0) = 0$. Write $r_{n,k}$ for the coefficient of $x^n$
in $g f^k$, and suppose that for all natural numbers $n$ and $k$

$$r_{n+1,0} = (b + \varepsilon)\, r_{n,0} + (\lambda + \delta)\, r_{n,1},$$



$$r_{n+1,k+1} = r_{n,k} + b\, r_{n,k+1} + \lambda\, r_{n,k+2},$$

that is, the Riordan array $(g, f)$ has dot diagram
$[b + \varepsilon, \lambda + \delta; 1, b, \lambda]$. With the Riordan product
$(p_1, p_2) \ast (q_1, q_2) = (p_1 \cdot q_1(p_2),\, q_2(p_2))$, let
$P_b = \bigl(1/(1 - bx),\, x/(1 - bx)\bigr)$ and
$C_\lambda = \bigl(c(\lambda x^2),\, x\, c(\lambda x^2)\bigr)$, where
$c(x) = \sum_{m \ge 0} C_m x^m$ is the generating function of the Catalan numbers $C_m$, and let
$F_{\varepsilon,\delta} = \bigl(1/(1 - \varepsilon x - \delta x^2),\, x\bigr)$. Then
$(g, f) = (P_b \ast C_\lambda) \ast F_{\varepsilon,\delta}$.

## Sources

- Cameron and Nkwanta, Riordan multiplication at lines 113–117 and the dot-diagram recursions at lines 124–138.
- Naiomi T. Cameron and Asamoah Nkwanta, *On Some (Pseudo) Involutions in the Riordan Group*, Journal of Integer Sequences 8 (2005), Article 05.3.7, Triple Factorization theorem due to Peart and Woodson, line 339, reused in the proof at line 373, <https://cs.uwaterloo.ca/journals/JIS/VOL8/Cameron/cameron46.tex>.

Formalized by `MetaMathlibExt.triple_factorization_of_dot_diagram`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TripleFactorization.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TripleFactorization.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html#triple-factorization-of-dot-diagram).

## Twin Powers Theorem for pseudo-involutions

Let $l$ be a natural number, let
$n = 2l + 1$, and let $g$ be a formal power series over $\mathbb{R}$ with $g(0) \ne 0$. Put
$f(x) = x\, g(x^n)$ and $h(x) = x\, g(x)^n$. Call a power series $p$ pseudo-involutory if
$p(0) = 0$, the coefficient of $x$ in $p$ is nonzero, and the compositional inverse $\bar p$ of
$p$ satisfies $\bar p(x) = -p(-x)$; call $B$ a B-function of $p$ if
$p(x) - x = x\, p(x)\, B(x\, p(x))$. Let

$$P(x) = \sum_{j=0}^{l} \frac{2l+1}{2j+1} \binom{l+j}{2j} x^j.$$

Suppose that $B_f$ is a B-function of $f$, that $B_h$ is a B-function of $h$, and that $f$ or $h$
is pseudo-involutory. Then $f$ and $h$ are both pseudo-involutory, and

$$x^n B_h(x^n)^2 = x B_f(x)^2 \, P\bigl(x B_f(x)^2\bigr)^2.$$

## Sources

- Alexander Burstein and Louis W. Shapiro, "Pseudo-Involutions in the Riordan Group," Journal of Integer Sequences 25 (2022), Article 22.3.6, The Twin Powers Theorem, lines 1129–1146, https://cs.uwaterloo.ca/journals/JIS/VOL25/Burstein/burstein14.tex

Formalized by `MetaMathlibExt.twin_powers`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TwinPowers.lean, line 1144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TwinPowers.lean#L1144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html#twin-powers).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riordan arrays and number triangles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays)
