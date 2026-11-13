---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry4.ramanujan_part1_ch5_entry4, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry5Eulerianexplicit.ramanujan_part1_ch5_entry5_eulerianexplicit, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_exp_add_one_ne, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_psi_neg_one, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_psi_one, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_hasSum_bernoulli, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_hasSum_psi, MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.ramanujan_part1_ch5_entry8_eulerianformula
statement: formalized
proof: formalized
---

# Eulerian polynomials

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html).

## Eulerian polynomials and the series of (k+1)^n (-p)^k

Let $A(n,k)$ be the Eulerian
numbers, given by $A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$ and
$A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$, and let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$. For every natural
number $n$ and every complex number $p$ with $|p| < 1$, we have $p + 1 \ne 0$, the series
$\sum_{k \ge 0} (k+1)^n (-p)^k$ is summable, and
$\Psi_n(p)/(p+1)^{n+1} = \sum_{k=0}^{\infty} (k+1)^n (-p)^k$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5, Entry 4, p. 113.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry4.ramanujan_part1_ch5_entry4`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry4.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry4.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#ramanujan-part1-ch5-entry4).

## Two finite expansions of the Eulerian polynomials

Let $A(n,k)$ be the Eulerian numbers,
given by $A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$ and
$A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$, and let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$. For every integer
$n \ge 1$ and every complex number $p \ne -1$, we have $p + 1 \ne 0$, $\Psi_0(p) = 1$,
$(-1)^{n+1} p \, \Psi_n(p)/(p+1)^n = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \Psi_k(p)/(p+1)^k$, and
$\Psi_n(p) = \sum_{j=0}^{n-1} (-1)^j \binom{n}{j+1} (p+1)^j \Psi_{n-j-1}(p)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5, Entry 5, formulas (5.1) and (5.2).

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry5Eulerianexplicit.ramanujan_part1_ch5_entry5_eulerianexplicit`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry5Eulerianexplicit.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry5Eulerianexplicit.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#ramanujan-part1-ch5-entry5-eulerianexpli).

## No zeros of e^z + 1 in the disc of radius pi

For every complex number $z$ with
$|z| < \pi$, we have $e^z + 1 \ne 0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_exp_add_one_ne`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#chapter5-entry8-exp-add-one-ne).

## Eulerian polynomials at p = -1

Let $A(n,k)$ be the Eulerian numbers, given by
$A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$ and
$A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$, and let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$. For every natural
number $n$, $\Psi_n(-1) = n!$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_psi_neg_one`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#chapter5-entry8-psi-neg-one).

## Eulerian polynomials at p = 1 in terms of Bernoulli numbers

Let $A(n,k)$ be the Eulerian
numbers, given by $A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$ and
$A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$; let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$, and let $B_m$ be
the Bernoulli numbers. For every integer $n \ge 1$,
$\Psi_n(1) = 2^{n+1}(2^{n+1} - 1)B_{n+1}/(n+1)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_psi_one`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean, line 757](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean#L757). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#chapter5-entry8-psi-one).

## Bernoulli-number expansion of 1/(e^z + 1) in the disc of radius pi

Let $B_m$ be the
Bernoulli numbers, with $B_1 = -\tfrac{1}{2}$. For every complex number $z$ with $|z| < \pi$, the
series $\sum_{j \ge 0} (1 - 2^{j+1}) B_{j+1} z^j/(j+1)!$ is summable with sum $1/(e^z + 1)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_hasSum_bernoulli`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean, line 766](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean#L766). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#chapter5-entry8-has-sum-bernoulli).

## Eulerian-polynomial expansion of 1/(e^z + 1) in the disc of radius pi

Let $A(n,k)$ be the
Eulerian numbers, given by $A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$ and
$A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$, and let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$. For every complex
number $z$ with $|z| < \pi$, the series $\sum_{m \ge 0} (-1)^m \Psi_m(1) z^m/(2^{m+1} m!)$ is
summable with sum $1/(e^z + 1)$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.chapter5Entry8_hasSum_psi`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean, line 774](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean#L774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#chapter5-entry8-has-sum-psi).

## Eulerian polynomials at 1 and -1 and two series for 1/(e^z + 1)

Let $A(n,k)$ be the
Eulerian numbers, given by $A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$ and
$A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$; let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$, and let $B_m$ be
the Bernoulli numbers, with $B_1 = -\tfrac{1}{2}$. For every integer $n \ge 1$ and every complex
number $z$ with $|z| < \pi$, we have $e^z + 1 \ne 0$, $\Psi_n(-1) = n!$,
$\Psi_n(1) = 2^{n+1}(2^{n+1} - 1)B_{n+1}/(n+1)$, the series
$\sum_{j \ge 0} (1 - 2^{j+1}) B_{j+1} z^j/(j+1)!$ is summable with sum $1/(e^z + 1)$, and the
series $\sum_{m \ge 0} (-1)^m \Psi_m(1) z^m/(2^{m+1} m!)$ is summable with sum $1/(e^z + 1)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5, Entry 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry8Eulerianformula.ramanujan_part1_ch5_entry8_eulerianformula`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean, line 786](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry8Eulerianformula.lean#L786). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#ramanujan-part1-ch5-entry8-eulerianformu).

## Eulerian polynomials at 1 and -1 and two series for 1/(e^z + 1), under the old Entry 3 label

**Eulerian polynomials at 1 and -1 and two series for 1/(e^z + 1), under the old Entry 3
label.** Let $A(n,k)$ be the Eulerian numbers, given by $A(0,0) = 1$, $A(0,k) = 0$ for $k \ge 1$
and $A(n+1,k) = (k+1)A(n,k) + (n+1-k)A(n,k-1)$, where the last term is $0$ when $k = 0$; let
$\Psi_0(p) = 1$ and $\Psi_n(p) = \sum_{k=0}^{n-1} A(n,k)(-p)^k$ for $n \ge 1$, and let $B_m$ be
the Bernoulli numbers, with $B_1 = -\tfrac{1}{2}$. For every integer $n \ge 1$ and every complex
number $z$ with $|z| < \pi$, we have $e^z + 1 \ne 0$, $\Psi_n(-1) = n!$,
$\Psi_n(1) = 2^{n+1}(2^{n+1} - 1)B_{n+1}/(n+1)$, the series
$\sum_{j \ge 0} (1 - 2^{j+1}) B_{j+1} z^j/(j+1)!$ is summable with sum $1/(e^z + 1)$, and the
series $\sum_{m \ge 0} (-1)^m \Psi_m(1) z^m/(2^{m+1} m!)$ is summable with sum $1/(e^z + 1)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 5, Entry 8.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch5.Entry3Eulerianformula.ramanujan_part1_ch5_entry3_eulerianformula`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch5Entry3Eulerianformula.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch5Entry3Eulerianformula.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html#ramanujan-part1-ch5-entry3-eulerianformu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eulerian polynomials](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/eulerian-polynomials)
