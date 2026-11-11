---
declaration: section
origin: cited
lean: MetaMathlibExt.quaternaryRep_one_one_ten_ten_and_two_two_five_five, MetaMathlibExt.quaternaryRep_one_one_fifteen_fifteen_three_three_five_five_one_three_five_fifteen, MetaMathlibExt.phi_sq_phi_sq_ten_add_five_phi_sq_two_phi_sq_five, MetaMathlibExt.phi_sq_mul_phi_sq_ten_eisenstein, MetaMathlibExt.phi_sq_two_mul_phi_sq_five_eisenstein, MetaMathlibExt.twelve_phi_sq_phi_sq_ten_add_twelve_phi_sq_two_phi_sq_five, MetaMathlibExt.phi_sq_mul_phi_sq_fifteen_eisenstein, MetaMathlibExt.q_mul_ramanujanF_one_three_five_fifteen
statement: formalized
---

# Representation numbers of quaternary quadratic forms

10 results, 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html).

## Representation numbers of the quaternary forms $(1,1,10,10)$ and $(2,2,5,5)$

For a complex number $q$ write $f_k = \prod_{m \ge 1} (1 - q^{km})$. For
integers $a, b, c, d$ and $n$, let $N(a,b,c,d;n)$ be the number of $(x_1, x_2, x_3, x_4) \in
\mathbb{Z}^4$ with $a x_1^2 + b x_2^2 + c x_3^2 + d x_4^2 = n$, and let $\sigma(n/k)$ be the sum
of the positive divisors of $n/k$ if $k \mid n$ and $0$ otherwise. Let $b_1, b_2, b_3$ be sequences
of complex numbers indexed by $n \ge 0$ such that for every complex $q$ with $|q| < 1$ the
series $\sum_{n \ge 0} b_i(n) q^n$ converge, with sums $q f_2^2 f_{10}^2$, $q^2 f_4^2 f_{20}^2$
and $q^3 f_4^5 f_{10} f_{40}^2 / (f_2 f_8^2 f_{20})$ for $i = 1, 2, 3$ respectively. For
$n \ge 1$ put

$$
T(n) = \tfrac{2}{3}\sigma(n) - \tfrac{2}{3}\sigma(n/2) + \tfrac{4}{3}\sigma(n/4) +
\tfrac{10}{3}\sigma(n/5) - \tfrac{16}{3}\sigma(n/8) - \tfrac{10}{3}\sigma(n/10) +
\tfrac{20}{3}\sigma(n/20) - \tfrac{80}{3}\sigma(n/40).
$$

Then for every $n \ge 1$,

$$
N(1,1,10,10;n) = T(n) + \tfrac{10}{3} b_1(n) + \tfrac{8}{3} b_2(n) + 4b_3(n)
$$

and

$$
N(2,2,5,5;n) = T(n) - \tfrac{2}{3} b_1(n) + \tfrac{8}{3} b_2(n) - 4b_3(n).
$$

With $\eta_k = q^{k/24} f_k$, the three generating functions are the eta quotients
$\eta_2^2\eta_{10}^2$, $\eta_4^2\eta_{20}^2$ and
$\eta_4^5\eta_{10}\eta_{40}^2/(\eta_2\eta_8^2\eta_{20})$. These formulas are due to Alaca and
Altiary; Vasuki and Nagendra reprove them elementarily.

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Theorem 1.1 (Alaca and Altiary).

Stated but not proved: `MetaMathlibExt.quaternaryRep_one_one_ten_ten_and_two_two_five_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#quaternary-rep-one-one-ten-ten-and-two-t).

## Representation numbers of the quaternary forms $(1,1,15,15)$, $(3,3,5,5)$ and $(1,3,5,15)$

**Representation numbers of the quaternary forms $(1,1,15,15)$, $(3,3,5,5)$ and
$(1,3,5,15)$.** For a complex number $q$ write $f_k = \prod_{m \ge 1} (1 - q^{km})$. For
integers $a, b, c, d$ and $n$, let $N(a,b,c,d;n)$ be the number of $(x_1, x_2, x_3, x_4) \in
\mathbb{Z}^4$ with $a x_1^2 + b x_2^2 + c x_3^2 + d x_4^2 = n$, and let $\sigma(n/k)$ be the sum
of the positive divisors of $n/k$ if $k \mid n$ and $0$ otherwise. Let $a_1, \dots, a_5$ be
sequences of complex numbers indexed by $n \ge 0$ such that for every complex $q$ with
$|q| < 1$ the series $\sum_{n \ge 0} a_i(n) q^n$ converge, with sums $q f_1 f_3 f_5 f_{15}$,
$q^2 f_2 f_6 f_{10} f_{30}$, $q^4 f_4 f_{12} f_{20} f_{60}$, $q f_3 f_5 f_6 f_{10}$ and
$q^2 f_6 f_{10} f_{12} f_{20}$ for $i = 1, \dots, 5$ respectively. For $n \ge 1$ put

$$
S(n) = \tfrac{2}{3}\sigma(n) - \tfrac{4}{3}\sigma(n/2) + \tfrac{8}{3}\sigma(n/4) - 2\sigma(n/3) +
4\sigma(n/6) - 8\sigma(n/12) + \tfrac{10}{3}\sigma(n/5) - \tfrac{20}{3}\sigma(n/10) +
\tfrac{40}{3}\sigma(n/20) - 10\sigma(n/15) + 20\sigma(n/30) - 40\sigma(n/60).
$$

Then for every $n \ge 1$,

$$
N(1,1,15,15;n) = S(n) + \tfrac{2}{3}(a_1(n) - 2a_2(n) + 4a_3(n) + 4a_4(n) + 8a_5(n)),
$$



$$
N(3,3,5,5;n) = S(n) + \tfrac{2}{3}(-5a_1(n) - 14a_2(n) - 20a_3(n) + 4a_4(n) + 8a_5(n))
$$

and

$$
N(1,3,5,15;n) = \tfrac{1}{2}(\sigma(n) - 2\sigma(n/2) + 4\sigma(n/4) + 3\sigma(n/3) -
6\sigma(n/6) + 12\sigma(n/12) - 5\sigma(n/5) + 10\sigma(n/10) - 20\sigma(n/20) -
15\sigma(n/15) + 30\sigma(n/30) - 60\sigma(n/60)) + \tfrac{3}{2} a_1(n) + a_2(n) + 6a_3(n).
$$

With $\eta_k = q^{k/24} f_k$, the five generating functions are the eta quotients
$\eta_1\eta_3\eta_5\eta_{15}$, $\eta_2\eta_6\eta_{10}\eta_{30}$,
$\eta_4\eta_{12}\eta_{20}\eta_{60}$, $\eta_3\eta_5\eta_6\eta_{10}$ and
$\eta_6\eta_{10}\eta_{12}\eta_{20}$. These formulas are due to Alaca; Vasuki and Nagendra
reprove them elementarily.

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Theorem 1.2 (Alaca).

Stated but not proved: `MetaMathlibExt.quaternaryRep_one_one_fifteen_fifteen_three_three_five_five_one_three_five_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#quaternary-rep-one-one-fifteen-fifteen-t).

## A theta identity for $\varphi(q)^2\varphi(q^{10})^2 + 5\varphi(q^2)^2\varphi(q^5)^2$

Let $q$ be a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$
and $\psi(x) = \sum_{n \ge 0} x^{n(n+1)/2}$ for Ramanujan's theta functions, and
$f_k = \prod_{m \ge 1} (1 - q^{km})$. Then

$$
\varphi(q)^2\varphi(q^{10})^2 + 5\varphi(q^2)^2\varphi(q^5)^2 = \varphi(q^2)^4 +
5\varphi(q^{10})^4 + 4q\psi(q^2)^4 + 20q^5\psi(q^{10})^4 + 16q^2 f_4^2 f_{20}^2 -
16q^3 \frac{f_4^5 f_{10} f_{40}^2}{f_2 f_8^2 f_{20}}.
$$

The power $q^3$ of the last term is not legible in the available text of the paper; it is the
one consistent with Theorem 1.1 and with Equation (3.13).

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 3.1.

Stated but not proved: `MetaMathlibExt.phi_sq_phi_sq_ten_add_five_phi_sq_two_phi_sq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#phi-sq-phi-sq-ten-add-five-phi-sq-two-ph).

## Eisenstein-series formula for $\varphi(q)^2\varphi(q^{10})^2$

Let $q$ be
a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$ for
Ramanujan's theta function, $f_k = \prod_{m \ge 1} (1 - q^{km})$, and $P_k = P(q^k)$, where
$P(x) = 1 - 24 \sum_{m \ge 1} m x^m / (1 - x^m)$ is the weight-two Eisenstein series. Then

$$
\varphi(q)^2\varphi(q^{10})^2 = -\tfrac{1}{36}(P_1 - P_2 + 2P_4 + 5P_5 - 8P_8 - 5P_{10} + 10P_{20} -
40P_{40}) + \tfrac{10}{3} q f_2^2 f_{10}^2 + \tfrac{8}{3} q^2 f_4^2 f_{20}^2 +
4q^3 \frac{f_4^5 f_{10} f_{40}^2}{f_2 f_8^2 f_{20}}.
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 3.3, Equation (3.13).

Stated but not proved: `MetaMathlibExt.phi_sq_mul_phi_sq_ten_eisenstein` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#phi-sq-mul-phi-sq-ten-eisenstein).

## Eisenstein-series formula for $\varphi(q^2)^2\varphi(q^5)^2$

Let $q$ be
a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$ for
Ramanujan's theta function, $f_k = \prod_{m \ge 1} (1 - q^{km})$, and $P_k = P(q^k)$, where
$P(x) = 1 - 24 \sum_{m \ge 1} m x^m / (1 - x^m)$ is the weight-two Eisenstein series. Then

$$
\varphi(q^2)^2\varphi(q^5)^2 = -\tfrac{1}{36}(P_1 - P_2 + 2P_4 + 5P_5 - 8P_8 - 5P_{10} + 10P_{20} -
40P_{40}) - \tfrac{2}{3} q f_2^2 f_{10}^2 + \tfrac{8}{3} q^2 f_4^2 f_{20}^2 -
4q^3 \frac{f_4^5 f_{10} f_{40}^2}{f_2 f_8^2 f_{20}}.
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 3.3, Equation (3.14).

Stated but not proved: `MetaMathlibExt.phi_sq_two_mul_phi_sq_five_eisenstein` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#phi-sq-two-mul-phi-sq-five-eisenstein).

## A theta identity for $12\varphi(q)^2\varphi(q^{10})^2 + 12\varphi(q^2)^2\varphi(q^5)^2$

Let $q$ be a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$
for Ramanujan's theta function and $f_k = \prod_{m \ge 1} (1 - q^{km})$. Then

$$
12\varphi(q)^2\varphi(q^{10})^2 + 12\varphi(q^2)^2\varphi(q^5)^2 = \varphi(q)^4 + 5\varphi(q^5)^4 +
4\varphi(q^2)^4 + 20\varphi(q^{10})^4 - \varphi(-q)^4 - 5\varphi(-q^5)^4 +
32q f_2^2 f_{10}^2 + 64q^2 f_4^2 f_{20}^2.
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 3.2.

Stated but not proved: `MetaMathlibExt.twelve_phi_sq_phi_sq_ten_add_twelve_phi_sq_two_phi_sq_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#twelve-phi-sq-phi-sq-ten-add-twelve-phi).

## Eisenstein-series formula for $\varphi(q)^2\varphi(q^{15})^2$

Let $q$ be
a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$ for
Ramanujan's theta function, $f_k = \prod_{m \ge 1} (1 - q^{km})$, and $P_k = P(q^k)$, where
$P(x) = 1 - 24 \sum_{m \ge 1} m x^m / (1 - x^m)$ is the weight-two Eisenstein series. Then

$$
\varphi(q)^2\varphi(q^{15})^2 = -\tfrac{1}{36}(P_1 - 2P_2 - 3P_3 + 4P_4 + 5P_5 + 6P_6 - 10P_{10} -
12P_{12} - 15P_{15} + 20P_{20} + 30P_{30} - 60P_{60}) + \tfrac{2}{3}(q f_1 f_3 f_5 f_{15} -
2q^2 f_2 f_6 f_{10} f_{30} + 4q^4 f_4 f_{12} f_{20} f_{60} + 4q f_3 f_5 f_6 f_{10} +
8q^2 f_6 f_{10} f_{12} f_{20}).
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 4.2.

Stated but not proved: `MetaMathlibExt.phi_sq_mul_phi_sq_fifteen_eisenstein` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#phi-sq-mul-phi-sq-fifteen-eisenstein).

## A product identity for Ramanujan's $f(q)f(q^3)f(q^5)f(q^{15})$

Let $q$ be a complex
number with $|q| < 1$. Write $f_k = \prod_{m \ge 1} (1 - q^{km})$, and let
$f(x) = \prod_{m \ge 1} (1 - (-x)^m) = (-x; -x)_\infty$ be Ramanujan's function. Then

$$
q f(q) f(q^3) f(q^5) f(q^{15}) = q f_1 f_3 f_5 f_{15} + 2q^2 f_2 f_6 f_{10} f_{30} +
4q^4 f_4 f_{12} f_{20} f_{60}.
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 4.3.

Stated but not proved: `MetaMathlibExt.q_mul_ramanujanF_one_three_five_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#q-mul-ramanujan-f-one-three-five-fifteen).

## Eisenstein-series formula for $\varphi(q^3)^2\varphi(q^5)^2$

Let $q$ be
a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$ for
Ramanujan's theta function, $f_k = \prod_{m \ge 1} (1 - q^{km})$, and $P_k = P(q^k)$, where
$P(x) = 1 - 24 \sum_{m \ge 1} m x^m / (1 - x^m)$ is the weight-two Eisenstein series. Then

$$
\varphi(q^3)^2\varphi(q^5)^2 = -\tfrac{1}{36}(P_1 - 2P_2 - 3P_3 + 4P_4 + 5P_5 + 6P_6 - 10P_{10} -
12P_{12} - 15P_{15} + 20P_{20} + 30P_{30} - 60P_{60}) - \tfrac{2}{3}(5q f_1 f_3 f_5 f_{15} +
14q^2 f_2 f_6 f_{10} f_{30} + 20q^4 f_4 f_{12} f_{20} f_{60} - 4q f_3 f_5 f_6 f_{10} -
8q^2 f_6 f_{10} f_{12} f_{20}).
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 4.4.

Stated but not proved: `MetaMathlibExt.phi_sq_three_mul_phi_sq_five_eisenstein` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#phi-sq-three-mul-phi-sq-five-eisenstein).

## Eisenstein-series formula for $\varphi(q)\varphi(q^3)\varphi(q^5)\varphi(q^{15})$

Let $q$
be a complex number with $|q| < 1$. Write $\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$ for
Ramanujan's theta function, $f_k = \prod_{m \ge 1} (1 - q^{km})$, and $P_k = P(q^k)$, where
$P(x) = 1 - 24 \sum_{m \ge 1} m x^m / (1 - x^m)$ is the weight-two Eisenstein series. Then

$$
\varphi(q)\varphi(q^3)\varphi(q^5)\varphi(q^{15}) = -\tfrac{1}{48}(P_1 - 2P_2 + 3P_3 + 4P_4 -
5P_5 - 6P_6 + 10P_{10} + 12P_{12} - 15P_{15} - 20P_{20} + 30P_{30} - 60P_{60}) +
\tfrac{3}{2} q f_1 f_3 f_5 f_{15} + q^2 f_2 f_6 f_{10} f_{30} + 6q^4 f_4 f_{12} f_{20} f_{60}.
$$

## Sources

- K. R. Vasuki and P. Nagendra, *On Certain Quaternary Quadratic Forms*, INTEGERS 25 (2025), Article A24, Lemma 4.6.

Stated but not proved: `MetaMathlibExt.phi_mul_phi_three_mul_phi_five_mul_phi_fifteen_eisenstein` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuaternaryQuadraticFormsWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html#phi-mul-phi-three-mul-phi-five-mul-phi-f).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representation numbers of quaternary quadratic forms](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representation-numbers-of-quaternary-quadratic-f)
