---
declaration: section
origin: cited
lean: MetaMathlibExt.ramanujanTheta_mul_add_mul_neg, MetaMathlibExt.ramanujanTheta_mul_sub_mul_neg, MetaMathlibExt.ramanujanTheta_one_five, MetaMathlibExt.ramanujanTheta_order_nine_product, MetaMathlibExt.ramanujanTheta_one_two, MetaMathlibExt.ramanujanTheta_eta_quotients, MetaMathlibExt.slaterOrderEighteen_modular_relations, MetaMathlibExt.slaterOrderEighteen_nonic_relations
statement: formalized
---

# Rogers–Ramanujan–Slater functions of order eighteen

8 results, 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html).

## Ramanujan's theta function: sum of products when $ab = cd$

Let
$f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function. For
complex numbers $a, b, c, d$ with $ab = cd$ and $|ab| < 1$,
$f(a,b) f(c,d) + f(-a,-b) f(-c,-d) = 2 f(ac,bd) f(ad,bc)$.

This is Entry 29(i) of Berndt's *Ramanujan's Notebooks*; the hypothesis $|ab| < 1$ makes all
the theta series converge.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Lemma 2, Equation (6).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_mul_add_mul_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#ramanujan-theta-mul-add-mul-neg).

## Ramanujan's theta function: difference of products when $ab = cd$

Let
$f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function. For
complex numbers $a, b, c, d$ with $ab = cd$, $|ab| < 1$, $c \ne 0$ and $d \ne 0$,
$f(a,b) f(c,d) - f(-a,-b) f(-c,-d) = 2a \, f(b/c, ac^2 d) \, f(b/d, acd^2)$.

This is Entry 29(ii) of Berndt's *Ramanujan's Notebooks*, where the second arguments are written
$(c/b)abcd = ac^2 d$ and $(d/b)abcd = acd^2$.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Lemma 2, Equation (7).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_mul_sub_mul_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#ramanujan-theta-mul-sub-mul-neg).

## Ramanujan's theta function at $(q, q^5)$

Let
$f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function and
$(a;q)_\infty = \prod_{n \ge 0} (1 - a q^n)$. For every complex number $q$ with $|q| < 1$,
$f(q,q^5) = (-q;q^2)_\infty \, f(-q^3,-q^9)$, that is, $f(q,q^5) = \chi(q) \psi(-q^3)$ with
$\chi(q) = (-q;q^2)_\infty$ and $\psi(q) = f(q,q^3)$.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Lemma 3, Equation (9).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_one_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#ramanujan-theta-one-five).

## Product of the nonic theta functions

Let
$f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function and
write $f(-x) = f(-x,-x^2)$. For every complex number $q$ with $|q| < 1$,
$f(-q,-q^8) f(-q^2,-q^7) f(-q^4,-q^5) f(-q^3) = f(-q) f(-q^9)^3$, that is,
$f(-q,-q^8) f(-q^2,-q^7) f(-q^4,-q^5) = f(-q) f^3(-q^9)/f(-q^3)$ with the denominator cleared.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Lemma 4, Equation (10).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_order_nine_product` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#ramanujan-theta-order-nine-product).

## Ramanujan's theta function at $(q, q^2)$

Let
$f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function and
$(a;q)_\infty = \prod_{n \ge 0} (1 - a q^n)$. For every complex number $q$ with $|q| < 1$,
$f(q,q^2) \, (q;q^2)_\infty = f(-q^3,-q^3)$, that is, $f(q,q^2) = \varphi(-q^3)/\chi(-q)$ with
the denominator cleared, where $\varphi(q) = f(q,q)$ and $\chi(-q) = (q;q^2)_\infty$.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Lemma 5, Equation (11).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_one_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#ramanujan-theta-one-two).

## Eta-quotients of Ramanujan's theta functions

Let $q$ be a complex number with
$|q| < 1$. Write $(a;q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ and $f_k = (q^k;q^k)_\infty$, and
let $f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's theta function.
Then $f(q,q) f_1^2 f_4^2 = f_2^5$, $f(q,q^3) f_1 = f_2^2$, $f(-q,-q) f_2 = f_1^2$,
$f(-q,-q^3) f_2 = f_1 f_4$, $f(q,-q^2) f_1 f_4 = f_2^3$, $(-q;q^2)_\infty f_1 f_4 = f_2^2$ and
$(q;q^2)_\infty f_2 = f_1$.

These are the classical eta-quotients $\varphi(q) = f_2^5/(f_1^2 f_4^2)$, $\psi(q) = f_2^2/f_1$,
$\varphi(-q) = f_1^2/f_2$, $\psi(-q) = f_1 f_4/f_2$, $f(q) = f_2^3/(f_1 f_4)$,
$\chi(q) = f_2^2/(f_1 f_4)$ and $\chi(-q) = f_1/f_2$ with the denominators cleared, where
$\varphi(q) = f(q,q)$, $\psi(q) = f(q,q^3)$, $f(q) = f(q,-q^2)$ and $\chi(q) = (-q;q^2)_\infty$.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Lemma 1 (quoted from Berndt).

Stated but not proved: `MetaMathlibExt.ramanujanTheta_eta_quotients` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#ramanujan-theta-eta-quotients).

## Modular relations for the order-eighteen Rogers–Ramanujan–Slater functions

Let $q$ be
a complex number with $0 < |q| < 1$. Write $(a;q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ and
$f_k = (q^k;q^k)_\infty$, let $f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be
Ramanujan's theta function, and set $P_n = f(-q^{7n},-q^{11n})/f_{6n}$,
$Q_n = f(-q^{5n},-q^{13n})/f_{6n}$ and $R_n = f(-q^n,-q^{17n})/f_{6n}$. Then the following seven
relations hold.

$$P_1 P_8 + q^3 Q_1 Q_8 + q^{15} R_1 R_8 = \frac{1}{2q f_6 f_{48}} \left(
\frac{f_2^5 f_8^2}{f_1^2 f_4^2 f_{16}} - \frac{f_9^2 f_{72}^2}{f_{18} f_{144}}\right) -
q^8 \frac{f_3 f_{18}^2 f_{24} f_{144}^2}{f_6^2 f_9 f_{48}^2 f_{72}}$$



$$P_2 P_7 + q^3 Q_2 Q_7 + q^{15} R_2 R_7 = \frac{1}{2q f_{12} f_{42}} \left(
\frac{f_2^5 f_{14}^2}{f_1^2 f_4^2 f_{28}} - \frac{f_{18}^2 f_{63}^2}{f_{36} f_{126}}\right) -
q^8 \frac{f_6 f_{21} f_{36}^2 f_{126}^2}{f_{12}^2 f_{18} f_{42}^2 f_{63}}$$



$$P_3 P_6 + q^3 Q_3 Q_6 + q^{15} R_3 R_6 = \frac{1}{2q} \left(
\frac{f_2^5 f_{18}}{f_1^2 f_4^2 f_{36}^2} - \frac{f_{27}^2 f_{54}^2}{f_{18} f_{36} f_{54} f_{108}}
\right) - q^8 \frac{f_9 f_{54}^2 f_{108}^2}{f_{18} f_{27} f_{36}^2 f_{54}}$$



$$P_4 P_5 + q^3 Q_4 Q_5 + q^{15} R_4 R_5 = \frac{1}{2q f_{24} f_{30}} \left(
\frac{f_2^5 f_{20}^2}{f_1^2 f_4^2 f_{40}} - \frac{f_{36}^2 f_{45}^2}{f_{72} f_{90}}\right) -
q^8 \frac{f_{12} f_{15} f_{72}^2 f_{90}^2}{f_{24}^2 f_{30}^2 f_{36} f_{45}}$$



$$P_1 Q_2 - q^3 Q_1 R_2 + q R_1 P_2 = \frac{1}{2q f_6 f_{12}} \left(
\frac{f_9^2 f_{18}}{f_{36}} - \frac{f_1^2 f_2}{f_4}\right) +
q^2 \frac{f_3 f_{18} f_{36}^2}{f_6 f_9 f_{12}^2}$$



$$q^5 P_1 Q_{20} - q^{32} Q_1 R_{20} + R_1 P_{20} = \frac{1}{2q^4 f_6 f_{120}} \left(
\frac{f_9^2 f_{180}^2}{f_{18} f_{360}} - \frac{f_4^2 f_{10}^5}{f_5^2 f_8 f_{20}^2}\right) +
q^{17} \frac{f_3 f_{18}^2 f_{60} f_{360}^2}{f_6^2 f_9 f_{120}^2 f_{180}}$$



$$q^{23} P_1 R_{14} + Q_1 P_{14} - q^6 R_1 Q_{14} = \frac{1}{2q^2 f_6 f_{84}} \left(
\frac{f_9^2 f_{126}^2}{f_{18} f_{252}} - \frac{f_2^2 f_{14}^5}{f_4 f_7^2 f_{28}^2}\right) +
q^{13} \frac{f_3 f_{18}^2 f_{42} f_{252}^2}{f_6^2 f_9 f_{84}^2 f_{126}}$$

These are the source's relations (12)–(18), in order, for $P_n = P(q^n)$, $Q_n = Q(q^n)$ and
$R_n = R(q^n)$, where $P(q) = f(-q^7,-q^{11})/f(-q^6)$, $Q(q) = f(-q^5,-q^{13})/f(-q^6)$ and
$R(q) = f(-q,-q^{17})/f(-q^6)$ are the order-eighteen functions and $f(-q^6) = f_6$.

Deviation: in (14), the third relation, the paper prints $f_{48}$ in the last denominator; that
is false (the coefficients of $q^{56}$ of the two sides are $0$ and $-1$). The statement uses
$f_{54}$, the $f_{6n}$ factor that (12), (13) and (15) carry at this place ($f_{48} = f_{6 \cdot 8}$
is the value from (12)); with $f_{54}$ the relation checks exactly through $q^{198}$.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Theorem 1, Equations (12)-(18).

Stated but not proved: `MetaMathlibExt.slaterOrderEighteen_modular_relations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#slater-order-eighteen-modular-relations).

## Relations between the order-eighteen and the nonic Rogers–Ramanujan functions

Let $q$
be a complex number with $|q| < 1$. Write $(a;q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ and
$f_k = (q^k;q^k)_\infty$, let $f(a,b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be
Ramanujan's theta function, and set $P_n = f(-q^{7n},-q^{11n})/f_{6n}$,
$Q_n = f(-q^{5n},-q^{13n})/f_{6n}$, $R_n = f(-q^n,-q^{17n})/f_{6n}$,
$A_n = f(-q^{4n},-q^{5n})/f_{3n}$, $B_n = f(-q^{2n},-q^{7n})/f_{3n}$ and
$C_n = f(-q^n,-q^{8n})/f_{3n}$. Then

$$P_1 Q_1 R_1 = \frac{(q;q^2)_\infty \, f_{18}^3}{(q^3;q^6)_\infty \, f_6^3},$$



$$\frac{P_1 A_2 + q^3 R_1 C_2}{A_1} = \frac{Q_1 A_2 - q^2 R_1 B_2}{B_1} =
\frac{P_1 B_2 - q Q_1 C_2}{C_1} = \frac{f_9^2}{f_6 f_{18}}$$

and

$$\frac{P_1 A_2 + Q_1 B_2 + q^3 R_1 C_2}{A_1} = \frac{Q_1 A_2 - q^2 R_1 B_2 + P_1 C_2}{B_1} =
\frac{R_1 A_2 + P_1 B_2 - q Q_1 C_2}{C_1} = \frac{f_9^2}{f_6 f_{18}} +
\frac{f_3 f_{18}^2}{f_6^2 f_9}.$$

These are the source's relations (21)–(27). Here $P_n$, $Q_n$, $R_n$ are the order-eighteen
functions of Theorem 1 and $A_n$, $B_n$, $C_n$ the nonic Rogers–Ramanujan functions
$A(q) = f(-q^4,-q^5)/f(-q^3)$, $B(q) = f(-q^2,-q^7)/f(-q^3)$, $C(q) = f(-q,-q^8)/f(-q^3)$
evaluated at $q^n$, with $f(-q^3) = f_3$; the first relation reads
$P_1 Q_1 R_1 = \chi(-q) f_{18}^3 / (\chi(-q^3) f_6^3)$ with $\chi(-q) = (q;q^2)_\infty$.

## Sources

- A. Vanitha, M. P. Chaudhary, and Madiha Khanum, *Modular Relations for the Rogers-Ramanujan-Slater Type Functions of Order Eighteen with Applications to Partitions*, INTEGERS 24 (2024), Article A103, Theorem 2, Equations (21)-(27).

Stated but not proved: `MetaMathlibExt.slaterOrderEighteen_nonic_relations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/SlaterOrderEighteenThetaWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html#slater-order-eighteen-nonic-relations).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rogers–Ramanujan–Slater functions of order eighteen](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/rogers-ramanujan-slater-functions-of-order-eight)
