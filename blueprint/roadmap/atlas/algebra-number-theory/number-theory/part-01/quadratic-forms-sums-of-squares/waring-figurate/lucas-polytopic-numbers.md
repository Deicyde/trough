---
declaration: section
origin: cited
lean: MetaMathlibExt.lucasBracketAux, MetaMathlibExt.LucasParameters, MetaMathlibExt.lucasBracket, MetaMathlibExt.lucasFactorial, MetaMathlibExt.lucasnomial, MetaMathlibExt.lucasPolytopicNumber, MetaMathlibExt.lucasTriangularNumber, MetaMathlibExt.lucasTetrahedralNumber
statement: formalized
---

# Lucas-polytopic numbers

25 results, 14 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html).

## Lucas brackets for arbitrary real parameters

For real numbers $s$ and $t$, this is the
sequence of real numbers $a_0, a_1, a_2, \dots$ defined by $a_0 = 0$, $a_1 = 1$ and
$a_{n+2} = s a_{n+1} + t a_n$ for every natural number $n$.

No condition is imposed on $s$ and $t$.

Formalized by `MetaMathlibExt.lucasBracketAux`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-bracket-aux).

## Nondegenerate Lucas parameters

For real numbers $s$ and $t$, let $\{n\}_{s,t}$ be the
sequence of real numbers with $\{0\}_{s,t} = 0$, $\{1\}_{s,t} = 1$ and
$\{n+2\}_{s,t} = s\{n+1\}_{s,t} + t\{n\}_{s,t}$ for every natural number $n$. Nondegenerate
Lucas parameters are a pair of real numbers $(s, t)$ with $s \ne 0$, $t \ne 0$ and
$\{n\}_{s,t} \ne 0$ for every natural number $n \ne 0$.

The last condition ensures that the $s,t$-factorials are nonzero, so quotients of them never
divide by zero.

Formalized by `MetaMathlibExt.LucasParameters`, a structure declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-parameters).

## Lucas brackets

For nondegenerate Lucas parameters $(s, t)$, the Lucas brackets are the
real numbers $\{n\}_{s,t}$, for natural numbers $n$, defined by $\{0\}_{s,t} = 0$,
$\{1\}_{s,t} = 1$ and $\{n+2\}_{s,t} = s\{n+1\}_{s,t} + t\{n\}_{s,t}$ for every natural
number $n$.

Formalized by `MetaMathlibExt.lucasBracket`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-bracket).

## Factorial of Lucas brackets

For nondegenerate Lucas parameters $(s, t)$, write
$\{k\}_{s,t}$ for the $k$-th Lucas bracket. For a natural number $n$, the $s,t$-factorial is the
real number $\{n\}_{s,t}! = \prod_{k=1}^{n} \{k\}_{s,t}$, the product of
$\{1\}_{s,t}, \dots, \{n\}_{s,t}$; for $n = 0$ it is the empty product $1$.

Formalized by `MetaMathlibExt.lucasFactorial`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-factorial).

## Lucasnomial coefficients

Let $(s, t)$ be nondegenerate Lucas parameters and write
$\{m\}_{s,t}!$ for the $s,t$-factorial of a natural number $m$. For natural numbers $n$ and
$k$, the Lucasnomial coefficient is the real number

$$\binom{n}{k}_{s,t} = \frac{\{n\}_{s,t}!}{\{k\}_{s,t}! \{n-k\}_{s,t}!}$$

when $k \le n$, and $\binom{n}{k}_{s,t} = 0$ when $k > n$.

Formalized by `MetaMathlibExt.lucasnomial`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucasnomial).

## Simplicial Lucas-polytopic numbers

For nondegenerate Lucas parameters $(s, t)$ and
natural numbers $n$ and $d$, the $n$-th simplicial $d$-Lucas-polytopic number is the
Lucasnomial coefficient $\binom{n+d-1}{d}_{s,t}$, where $n + d - 1$ is read as $0$ when
$n = d = 0$.

Formalized by `MetaMathlibExt.lucasPolytopicNumber`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-polytopic-number).

## Lucas triangular numbers

For nondegenerate Lucas parameters $(s, t)$ and a natural
number $n$, the $n$-th Lucas triangular number is the Lucasnomial coefficient
$\binom{n+1}{2}_{s,t}$.

Formalized by `MetaMathlibExt.lucasTriangularNumber`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-triangular-number).

## Lucas tetrahedral numbers

For nondegenerate Lucas parameters $(s, t)$ and a natural
number $n$, the $n$-th Lucas tetrahedral number is the Lucasnomial coefficient
$\binom{n+2}{3}_{s,t}$.

Formalized by `MetaMathlibExt.lucasTetrahedralNumber`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-tetrahedral-number).

## Lucas pentachoron numbers

For nondegenerate Lucas parameters $(s, t)$ and a natural
number $n$, the $n$-th Lucas pentachoron number is the Lucasnomial coefficient
$\binom{n+3}{4}_{s,t}$.

Formalized by `MetaMathlibExt.lucasPentachoronNumber`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-pentachoron-number).

## Lucas hexateron numbers

For nondegenerate Lucas parameters $(s, t)$ and a natural
number $n$, the $n$-th Lucas hexateron number is the Lucasnomial coefficient
$\binom{n+4}{5}_{s,t}$.

Formalized by `MetaMathlibExt.lucasHexateronNumber`, a definition declared in [MathlibExt/NumberTheory/LucasPolytopicNumber.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LucasPolytopicNumber.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-hexateron-number).

## Sum formula for Lucasnomial coefficients

Let $(s, t)$ be nondegenerate Lucas parameters,
with Lucasnomial coefficients $\binom{n}{k}_{s,t}$, and let $\varphi$ and $\varphi'$ be real
numbers with $\varphi + \varphi' = s$ and $\varphi \varphi' = -t$. For all natural numbers
$n \ge 1$ and $d$,

$$\binom{n+d}{d+1}_{s,t} = \sum_{k=1}^{n} \varphi^{(d+1)(n-k)} \varphi'^{k-1}
\binom{k+d-1}{d}_{s,t},$$

and the same holds with $\varphi$ and $\varphi'$ exchanged.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 2 (`jis-2025-25.5.6-thm-2`).

Stated but not proved: `MetaMathlibExt.lucasnomial_succ_eq_sum_lucasPolytopic` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucasnomial-succ-eq-sum-lucas-polytopic).

## Identities for the Lucas triangular numbers

Let $(s, t)$ be nondegenerate Lucas
parameters and let $\varphi, \varphi'$ be real numbers with $\varphi + \varphi' = s$ and
$\varphi\varphi' = -t$; write $\{n\}_{s,t}$ for the Lucas brackets and $\binom{n}{k}_{s,t}$ for
the Lucasnomial coefficients. Then
$\binom{n+1}{2}_{s,t} = t\binom{n}{2}_{s,t} + \{n\}_{s,t}^2$ and
$\binom{n+1}{2}_{s,t} = \sum_{k=1}^{n} t^{n-k}\{k\}_{s,t}^2$ for every natural number $n$, and
$\varphi'^{n-1}\binom{n+1}{2}_{s,t} + \varphi^{n+1}\binom{n}{2}_{s,t} =
\frac{\varphi^n + \varphi'^n}{\{2\}_{s,t}}\{n\}_{s,t}^2$ for every natural number $n \ge 1$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 3 (`jis-2025-25.5.6-thm-3`).

Stated but not proved: `MetaMathlibExt.lucasTriangular_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-triangular-identities).

## Weighted difference of consecutive squared Lucas triangular numbers

Let $(s, t)$ be
nondegenerate Lucas parameters, with Lucas brackets $\{n\}_{s,t}$ and Lucasnomial coefficients
$\binom{n}{k}_{s,t}$. For every natural number $n$,

$$\binom{n+2}{2}_{s,t}^{2} - t^2 \binom{n+1}{2}_{s,t}^{2} =
\frac{\{n+2\}_{s,t} + t \{n\}_{s,t}}{s} \{n+1\}_{s,t}^{3}.$$

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 4 (`jis-2025-25.5.6-thm-4`).

Stated but not proved: `MetaMathlibExt.lucasTriangular_sq_sub_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-triangular-sq-sub-sq).

## Weighted sum of cubes of Lucas brackets

Let $(s, t)$ be nondegenerate Lucas parameters,
with Lucas brackets $\{n\}_{s,t}$ and Lucasnomial coefficients $\binom{n}{k}_{s,t}$. For every
natural number $n$,

$$\sum_{k=1}^{n} t^{2(n-k)} \frac{\{k+1\}_{s,t} + t \{k-1\}_{s,t}}{s} \{k\}_{s,t}^{3} =
\binom{n+1}{2}_{s,t}^{2}.$$

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 5 (`jis-2025-25.5.6-thm-5`).

Stated but not proved: `MetaMathlibExt.sum_cubes_eq_lucasTriangular_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#sum-cubes-eq-lucas-triangular-sq).

## Sum-of-cubes identities for Fibonacci, Pell, Jacobsthal and Mersenne numbers

Let $F_n$
be the Fibonacci numbers, $P_n$ the Pell numbers, and $J_n$ the Jacobsthal numbers, that is, the
Lucas sequence $U(1, -2)$, with $J_0 = 0$, $J_1 = 1$ and $J_{n+2} = J_{n+1} + 2 J_n$. For every
natural number $n$,

$$\sum_{k=1}^{n} (F_{k+1} + F_{k-1}) F_k^3 = F_n^2 F_{n+1}^2,$$



$$\sum_{k=1}^{n} (P_{k+1} + P_{k-1}) P_k^3 = \tfrac{1}{2} P_n^2 P_{n+1}^2,$$



$$\sum_{k=1}^{n} 4^{n-k} (J_{k+1} + 2 J_{k-1}) J_k^3 = J_n^2 J_{n+1}^2,$$



$$\sum_{k=1}^{n} 4^{n-k} (2^k + 1) (2^k - 1)^3 = \tfrac{1}{3} (2^n - 1)^2 (2^{n+1} - 1)^2,$$

and, for every real number $q$ with $q \ne 1$ and $q \ne -1$ (Warnaar's identity),

$$\sum_{k=1}^{n} q^{2(n-k)} \frac{1 - q^{2k}}{1 - q^2} \Big(\frac{1 - q^k}{1 - q}\Big)^2 =
\Big(\frac{(1 - q^{n+1}) (1 - q^n)}{(1 - q) (1 - q^2)}\Big)^2.$$

The numbers $2^k - 1$ are the Mersenne numbers, and the right side of the last identity is the
square of the Gaussian binomial coefficient $\binom{n+1}{2}_q$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Corollary 6 (`jis-2025-25.5.6-cor-6`).

Stated but not proved: `MetaMathlibExt.sum_cubes_specializations` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#sum-cubes-specializations).

## Recurrence for the Lucas tetrahedral numbers

Let $(s, t)$ be nondegenerate Lucas
parameters, and write $\{n\}_{s,t}$ for the Lucas brackets and $\binom{n}{k}_{s,t}$ for the
Lucasnomial coefficients. For every natural number $n$,

$$\binom{n+3}{3}_{s,t} = st\binom{n+2}{3}_{s,t} + \{n+1\}_{s,t}\binom{n+2}{2}_{s,t}.$$

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 7 (`jis-2025-25.5.6-thm-7`).

Stated but not proved: `MetaMathlibExt.lucasTetrahedral_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-tetrahedral-recurrence).

## Lucas derivative

For real numbers $\varphi$ and $\varphi'$, the Lucas derivative
$D_{\varphi,\varphi'}$ sends a function $f : \mathbb{R} \to \mathbb{R}$ to the function whose
value at $x \ne 0$ is $(f(\varphi x) - f(\varphi' x))/((\varphi - \varphi')x)$, read as $0$ when
$\varphi = \varphi'$, and whose value at $0$ is the derivative $f'(0)$, read as $0$ when $f$ is
not differentiable at $0$.

In the paper $\varphi \ne \varphi'$ are the roots of $x^2 - sx - t$; its separate definition for
$s^2 + 4t = 0$ is not covered.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Section 2 (definition of the Lucas-derivative).

Formalized by `MetaMathlibExt.lucasDerivative`, a definition declared in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-derivative).

## The Lucas derivative away from the origin

For all real numbers $\varphi$, $\varphi'$
and $x \ne 0$ and every function $f : \mathbb{R} \to \mathbb{R}$, the Lucas derivative
$D_{\varphi,\varphi'}$ satisfies
$D_{\varphi,\varphi'} f(x) = (f(\varphi x) - f(\varphi' x))/((\varphi - \varphi')x)$, where the
quotient is read as $0$ when $\varphi = \varphi'$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Section 2 (definition of the Lucas-derivative).

Formalized by `MetaMathlibExt.lucasDerivative_of_ne_zero`, a theorem declared in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-derivative-of-ne-zero).

## The Lucas derivative at the origin

For all real numbers $\varphi$, $\varphi'$ and every
function $f : \mathbb{R} \to \mathbb{R}$, the Lucas derivative $D_{\varphi,\varphi'}$ satisfies
$D_{\varphi,\varphi'} f(0) = f'(0)$, where $f'(0)$ is read as $0$ when $f$ is not differentiable
at $0$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Section 2 (definition of the Lucas-derivative).

Formalized by `MetaMathlibExt.lucasDerivative_zero`, a theorem declared in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-derivative-zero).

## The Lucas derivative of the identity

For distinct real numbers $\varphi \ne \varphi'$,
the Lucas derivative $D_{\varphi,\varphi'}$ of the identity function $y \mapsto y$ equals $1$ at
every real number $x$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Section 2 (definition of the Lucas-derivative).

Formalized by `MetaMathlibExt.lucasDerivative_id`, a theorem declared in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-derivative-id).

## Iterated Lucas derivatives of $1/(1 - x)$

Let $(s, t)$ be nondegenerate Lucas
parameters, let $\varphi \ne \varphi'$ be real numbers with $\varphi + \varphi' = s$ and
$\varphi\varphi' = -t$, write $D_{\varphi,\varphi'}$ for the Lucas derivative and
$\{n\}_{s,t}!$ for the $s,t$-factorial. For every natural number $n$ and every real number $x$
with $\prod_{k=0}^{n} (1 - \varphi^{n-k}\varphi'^k x) \ne 0$, the $n$-fold iterate of
$D_{\varphi,\varphi'}$ applied to the function $y \mapsto 1/(1 - y)$ has value at $x$

$$\frac{\{n\}_{s,t}!}{\prod_{k=0}^{n} (1 - \varphi^{n-k}\varphi'^k x)}.$$

With $q = \varphi'/\varphi$ the denominator is the $q$-Pochhammer symbol
$(\varphi^n x; q)_{n+1}$ of the paper, which states the identity for $n \ge 1$. Real distinct
$\varphi, \varphi'$ exist only when $s^2 + 4t > 0$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 8 (`jis-2025-25.5.6-thm-8`).

Stated but not proved: `MetaMathlibExt.iterate_lucasDerivative_inv_one_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#iterate-lucas-derivative-inv-one-sub).

## Generating function of the simplicial Lucas-polytopic numbers

Let $(s, t)$ be
nondegenerate Lucas parameters, let $\varphi, \varphi'$ be real numbers with
$\varphi + \varphi' = s$ and $\varphi\varphi' = -t$, let $d$ be a natural number and write
$\binom{n}{k}_{s,t}$ for the Lucasnomial coefficients, so that the $n$-th simplicial
$d$-Lucas-polytopic number is $\binom{n+d-1}{d}_{s,t}$. Then, as formal power series in $x$ with
real coefficients,

$$\Big(\sum_{n\ge 1}\binom{n+d-1}{d}_{s,t}x^n\Big)\prod_{k=0}^{d}(1-\varphi^{d-k}\varphi'^k x)=x.$$

This is the paper's identity $\sum_{n \ge 1} \binom{n+d-1}{d}_{s,t} x^n = x/(\varphi^d x; q)_{d+1}$
with $q = \varphi'/\varphi$ and the denominator cleared.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 9 (`jis-2025-25.5.6-thm-9`).

Stated but not proved: `MetaMathlibExt.lucasPolytopic_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-polytopic-generating-function).

## Generating function of the squared Lucas triangular numbers

Let $(s, t)$ be nondegenerate
Lucas parameters, with Lucas brackets $\{n\}_{s,t}$ and Lucasnomial coefficients
$\binom{n}{k}_{s,t}$, and let $\varphi$ and $\varphi'$ be real numbers with
$\varphi + \varphi' = s$ and $\varphi \varphi' = -t$. Then, as formal power series in $x$ with
real coefficients,

$$\Big(\sum_{n \ge 1} \binom{n+1}{2}_{s,t}^{2} x^n\Big) (1 - t^2 x) (1 - \varphi'^4 x)
\prod_{k=0}^{3} (1 - \varphi^{4-k} \varphi'^k x) = x + (\{4\}_{s,t} \varphi - \varphi^4) x^2 -
\{3\}_{s,t} \varphi^3 \varphi'^3 x^3 +
(\{3\}_{s,t} \varphi^7 \varphi'^3 - \{4\}_{s,t} \varphi^6 \varphi'^3) x^4.$$

This is the paper's quotient formula for $\sum_{n \ge 1} \binom{n+1}{2}_{s,t}^{2} x^n$ with the
denominator cleared; the paper writes the product over $k$ as $(\varphi^4 x; q)_4$ with
$q = \varphi' / \varphi$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 10 (`jis-2025-25.5.6-thm-10`).

Stated but not proved: `MetaMathlibExt.lucasTriangular_sq_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#lucas-triangular-sq-generating-function).

## Even-index Lucas-bracket series as Lambert series

Let $(s, t)$ be nondegenerate Lucas
parameters with $s > 0$ and $s^2 + 4t > 0$, write $\{n\}_{s,t}$ for the Lucas brackets, let
$\varphi' = (s - \sqrt{s^2 + 4t})/2$ and let $L(x) = \sum_{n \ge 1} x^n/(1 - x^n)$ be the Lambert
series. Then the series $\sum_{n \ge 1} t^n/\{2n\}_{s,t}$ converges absolutely, and its sum is
$\sqrt{s^2 + 4t}\,\bigl(L(\varphi'^2/t) - L(\varphi'^4/t^2)\bigr)$.

The hypotheses make $\varphi'$ real with $|\varphi'| < (s + \sqrt{s^2 + 4t})/2$, so both Lambert
arguments lie in $(-1, 1)$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 11 (`jis-2025-25.5.6-thm-11`).

Stated but not proved: `MetaMathlibExt.hasSum_pow_div_lucasBracket_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#has-sum-pow-div-lucas-bracket-two-mul).

## Sum of reciprocals of products of consecutive Lucas brackets

Let $(s, t)$ be
nondegenerate Lucas parameters with $s > 0$, $s^2 + 4t > 0$ and $|t| > 1$, write $\{n\}_{s,t}$
for the Lucas brackets and let $\varphi = (s + \sqrt{s^2 + 4t})/2$. Then the series
$\sum_{n \ge 1} 1/(\{n\}_{s,t}\{n+1\}_{s,t})$ converges absolutely, and its sum is
$\varphi - (1 + t)\ln_{s,t}(1 + \varphi/t)$, where
$\ln_{s,t}(1 + \varphi/t) = -\sum_{n \ge 1} (-\varphi/t)^n/\{n\}_{s,t}$ is the Lucas logarithm.

The hypotheses $s > 0$ and $s^2 + 4t > 0$ make $\varphi$ real with $0 < |q| < 1$, where
$q = \varphi'/\varphi$ and $\varphi' = (s - \sqrt{s^2 + 4t})/2$; and $|t| > 1$ puts $-\varphi/t$ in
the paper's convergence range $(-|\varphi|, |\varphi|)$ of the Lucas logarithm. Without
$|t| > 1$ the logarithm series diverges: for $s = t = 1$ its terms $(-\varphi)^n/F_n$, with $F_n$
the Fibonacci numbers, do not tend to $0$.

## Sources

- Ronald Orozco López, *Simplicial d-Polytopic Numbers Defined on Lucas Sequences*, Journal of Integer Sequences 28 (2025), Article 25.5.6, Theorem 13 (`jis-2025-25.5.6-thm-13`).

Stated but not proved: `MetaMathlibExt.hasSum_inv_lucasBracket_mul_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LucasPolytopicNumberWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html#has-sum-inv-lucas-bracket-mul-succ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucas-polytopic numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/lucas-polytopic-numbers)
