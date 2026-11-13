---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Coding.CycleGraphCode.PositiveNat, MathlibExt.Combinatorics.Coding.CycleGraphCode.IsCycleCode, MathlibExt.Combinatorics.Coding.CycleGraphCode.CycleCode, MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleCode_finite, MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleCodeRate, MathlibExt.Combinatorics.Coding.CycleGraphCode.shannonCapacityCycle, MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleCodeRate_le_shannonCapacity, MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleConstruction_implies_lowerBound
statement: formalized
---

# Shannon capacity of a graph

77 results, 49 proved and 28 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html).

## Positive block lengths

The type of positive integers, that is, of natural numbers $n$
with $1 \le n$, used as the block lengths of codes.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.PositiveNat`, an abbreviation declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#positive-nat).

## Independent codes for the modular cycle

Let $q$ and $n$ be natural numbers. A finite set
$A$ of words of length $n$ over $\mathbb{Z}/q\mathbb{Z}$ is an independent code for the $q$-cycle
when every difference $x = a_1 - a_2$ with $a_1, a_2 \in A$ whose coordinates all lie in
$\{-1, 0, 1\}$ is the zero word. For $q \ge 3$ this says exactly that $A$ is an independent set
in the $n$-th strong power of the cycle graph $C_q$.

The source uses odd $q \ge 7$; the definition is stated for every $q$.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.IsCycleCode`, a definition declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#is-cycle-code).

## Cycle codes

For natural numbers $q$ and $n$, a cycle code of length $n$ modulo $q$ is a
finite set of words of length $n$ over $\mathbb{Z}/q\mathbb{Z}$ that is an independent code for
the $q$-cycle.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.CycleCode`, an abbreviation declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#cycle-code).

## Finitely many cycle codes of each length

For every nonzero natural number $q$ and every
natural number $n$, there are only finitely many cycle codes of length $n$ modulo $q$.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleCode_finite`, a theorem declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#cycle-code-finite).

## Rate of a cycle code

For a natural number $q$, a positive integer $n$ and a cycle code
$A$ of length $n$ modulo $q$, the rate of $A$ is $|A|^{1/n}$, the $n$-th root of the number of
codewords of $A$, taken in the extended nonnegative reals $[0, \infty]$.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleCodeRate`, a definition declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#cycle-code-rate).

## Shannon capacity of the modular cycle

For a natural number $q$, the Shannon capacity of
the $q$-cycle is the supremum, in $[0, \infty]$, of the rates $|A|^{1/n}$ over all positive
integers $n$ and all cycle codes $A$ of length $n$ modulo $q$.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.shannonCapacityCycle`, a definition declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#shannon-capacity-cycle).

## Code rates are at most the cycle capacity

For every natural number $q$, every positive
integer $n$ and every cycle code $A$ of length $n$ modulo $q$, the rate of $A$ is at most the
Shannon capacity of the $q$-cycle.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleCodeRate_le_shannonCapacity`, a theorem declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#cycle-code-rate-le-shannon-capacity).

## Codes give lower bounds on the cycle capacity

Let $q$, $n$ and $M$ be natural numbers
with $n \ge 1$. If some finite set of words of length $n$ over $\mathbb{Z}/q\mathbb{Z}$ is an
independent code for the $q$-cycle and has exactly $M$ elements, then $M^{1/n}$ is at most the
Shannon capacity of the $q$-cycle, as an inequality in $[0, \infty]$.

Formalized by `MathlibExt.Combinatorics.Coding.CycleGraphCode.cycleConstruction_implies_lowerBound`, a theorem declared in [MathlibExt/Combinatorics/Coding/CycleCode.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/CycleCode.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#cycle-construction-implies-lower-bound).

## Polak–Schrijver code of size 367 for the 7-cycle

There is a finite set $A$ of words of
length $5$ over $\mathbb{Z}/7\mathbb{Z}$ that is an independent code for the $7$-cycle and has
exactly $367$ elements.

## Sources

- Polak--Schrijver, arXiv:1808.07438, the fifth-power 367-word construction.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.polakSchrijverLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#polak-schrijver-lower-bound).

## Shannon's upper bound for the capacity of the 7-cycle

The Shannon capacity of the
$7$-cycle is at most $7/2$.

## Sources

- Shannon (1956), the fractional-clique-cover upper bound.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.shannon1956UpperBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#shannon1956-upper-bound).

## Lovász's theta value for the 7-cycle

This is the real number
$\frac{7 \cos(\pi/7)}{1 + \cos(\pi/7)}$, Lovász's closed form for the theta number of the
$7$-cycle, viewed as an element of $[0, \infty]$.

Approximate decimal displays of this number in the source are not asserted as equalities.

## Sources

- Lovász (1979), as printed in BPZ, arXiv:2607.29681.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.lovaszThetaCycleSeven`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#lovasz-theta-cycle-seven).

## Lovász's upper bound for the capacity of the 7-cycle

The Shannon capacity of the
$7$-cycle is at most $\frac{7 \cos(\pi/7)}{1 + \cos(\pi/7)}$, as an inequality in $[0, \infty]$.

## Sources

- Lovász (1979); the closed form is also printed in the retained BPZ primary.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.lovasz1979UpperBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#lovasz1979-upper-bound).

## Baumert et al. lower bound for the capacity of the 7-cycle

The Shannon capacity of the
$7$-cycle is at least $343^{1/5}$, as an inequality in $[0, \infty]$.

## Sources

- Baumert--McEliece--Rodemich--Rumsey--Stanley--Taylor (1971), exact rate row.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bmrrst1971LowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bmrrst1971-lower-bound).

## Vesel–Žerovnik lower bound for the capacity of the 7-cycle

The Shannon capacity of the
$7$-cycle is at least $108^{1/4}$.

## Sources

- Vesel--Žerovnik (2002), exact rate row; no unprinted code is supplied.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.veselZerovnik2002LowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#vesel-zerovnik2002-lower-bound).

## Mathew–Östergård lower bound for the capacity of the 7-cycle

The Shannon capacity of the
$7$-cycle is at least $350^{1/5}$, as an inequality in $[0, \infty]$.

## Sources

- Mathew--Östergård (2017), exact rate row; no unprinted code is supplied.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.mathewOstergard2017LowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#mathew-ostergard2017-lower-bound).

## Polak–Schrijver lower bound for the capacity of the 7-cycle

The Shannon capacity of the
$7$-cycle is at least $367^{1/5}$, as an inequality in $[0, \infty]$.

## Sources

- Polak--Schrijver, arXiv:1808.07438, exact fifth-root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.polakSchrijverRateLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#polak-schrijver-rate-lower-bound).

## Itty–Rosin–Carstensen–Reichman lower bound for the capacity of the 7-cycle

The Shannon
capacity of the $7$-cycle is at least $134753^{1/10}$, as an inequality in $[0, \infty]$.

## Sources

- Itty--Rosin--Carstensen--Reichman, arXiv:2607.21517, exact tenth-root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.ittyRosinCarstensenReichman2026LowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#itty-rosin-carstensen-reichman2026-lower).

## Itty–Rosin–Carstensen–Reichman code of dimension 10 for the 7-cycle

There is a finite
set $A$ of words of length $10$ over $\mathbb{Z}/7\mathbb{Z}$ that is an independent code for the
$7$-cycle and has exactly $134753$ elements.

## Sources

- Itty--Rosin--Carstensen--Reichman, arXiv:2607.21517, tenth-power construction.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.ittyRosinCarstensenReichman2026Construction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#itty-rosin-carstensen-reichman2026-const).

## BPZ profiles

A BPZ profile is an arbitrary quadruple of integers, called its code,
pairs, auxiliary and neutral coordinates: the four integer coordinates propagated by the
valid-tuple product of Buys, Polak and Zuiddam. No validity condition is imposed on the
quadruple.

## Sources

- BPZ, arXiv:2607.29681, valid-tuple profiles.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.BPZProfile`, a structure declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpzprofile).

## Product of BPZ profiles

For $i = 1, 2$ let $p_i = (c_i, \pi_i, a_i, z_i)$ be a BPZ
profile, with integer code, pairs, auxiliary and neutral coordinates. The product $p_1 \star p_2$
is the BPZ profile with code coordinate $(c_1 - \pi_1)(c_2 - \pi_2) + a_1 \pi_2 + \pi_1 a_2$,
pairs coordinate $z_1 \pi_2 + \pi_1 z_2$, auxiliary coordinate $a_1 a_2$ and neutral coordinate
$z_1 z_2 + (a_1 - z_1)(a_2 - z_2)$.

The product is arithmetic on the four coordinates only; it does not supply an independent set.

## Sources

- BPZ, arXiv:2607.29681, the profile product.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.BPZProfile.star`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#star).

## Iterated squaring of BPZ profiles

Write $\star$ for the BPZ profile product. For a
natural number $k$ and a BPZ profile $p$, the $k$-fold iterated square $S_k(p)$ is defined by
$S_0(p) = p$ and $S_{k+1}(p) = S_k(p \star p)$; that is, $S_k(p)$ is obtained from $p$ by
squaring $k$ times under $\star$.

## Sources

- BPZ, arXiv:2607.29681, iterated profile products.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzProfileSquareIter`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-profile-square-iter).

## Gao's code size in dimension 200

$M_{40}$ is the natural number
$4085567963379990282748597333793399773399910167372462
112610203714626938509773125898252337545387866277249$,
the cardinality Gao prints for a code of length $200$ for the $7$-cycle.

## Sources

- Gao, arXiv:2607.27869, the printed M40 value.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.gao2026M40`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#gao2026-m40).

## Gao's code of dimension 200 for the 7-cycle

Let $M_{40}$ be Gao's printed dimension-200
cardinality, a natural number with 103 decimal digits. There is a finite set $A$ of words of
length $200$ over $\mathbb{Z}/7\mathbb{Z}$ that is an independent code for the $7$-cycle and has
exactly $M_{40}$ elements.

## Sources

- Gao, arXiv:2607.27869, exact dimension-200 construction.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.gao2026Construction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#gao2026-construction).

## Gao's lower bound for the capacity of the 7-cycle

Let $M_{40}$ be Gao's printed
dimension-200 cardinality, a natural number with 103 decimal digits. The Shannon capacity of the
$7$-cycle is at least $M_{40}^{1/200}$, as an inequality in $[0, \infty]$.

## Sources

- Gao, arXiv:2607.27869, exact dimension-200 root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.gao2026LowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#gao2026-lower-bound).

## Buys–Polak–Zuiddam one-block profile for the 7-cycle

This is the Buys–Polak–Zuiddam
(BPZ) profile whose code, pairs, auxiliary and neutral coordinates are $367$, $8$, $367$ and $322$.

Only these four integers are recorded, not BPZ's five-dimensional construction behind them.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi1).

## Buys–Polak–Zuiddam two-block profile for the 7-cycle

This is $p_1 \star p_1$, where $p_1$
is the one-block 7-cycle profile, whose code, pairs, auxiliary and neutral coordinates are $367$,
$8$, $367$ and $322$, and $\star$ is the Buys–Polak–Zuiddam (BPZ) profile product.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi2`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi2).

## Three-block BPZ seven-cycle profile

A BPZ profile is a quadruple of integers
(code, pairs, auxiliary, neutral), and $\star$ denotes the BPZ profile product. The three-block
seven-cycle profile of Buys–Polak–Zuiddam is $\pi_3 = \pi_1 \star \pi_2$, where
$\pi_1 = (367, 8, 367, 322)$ is the one-block profile and $\pi_2 = \pi_1 \star \pi_1$ is the
two-block profile.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi3`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi3).

## Five-block BPZ seven-cycle profile

A BPZ profile is a quadruple of integers
(code, pairs, auxiliary, neutral), and $\star$ denotes the BPZ profile product. The five-block
seven-cycle profile of Buys–Polak–Zuiddam is $\pi_5 = \pi_2 \star \pi_3$, where
$\pi_1 = (367, 8, 367, 322)$, $\pi_2 = \pi_1 \star \pi_1$ and $\pi_3 = \pi_1 \star \pi_2$ are
the one-, two- and three-block profiles.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi5`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi5).

## Buys–Polak–Zuiddam ten-block profile for the 7-cycle

This is $p_5 \star p_5$, where $p_5$
is the five-block 7-cycle profile and $\star$ is the Buys–Polak–Zuiddam (BPZ) profile product.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi10`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi10).

## Buys–Polak–Zuiddam twenty-block profile for the 7-cycle

This is $p_{10} \star p_{10}$,
where $p_{10}$ is the ten-block 7-cycle profile and $\star$ is the Buys–Polak–Zuiddam (BPZ)
profile product.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi20`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi20).

## Forty-block BPZ seven-cycle profile

A BPZ profile is a quadruple of integers
(code, pairs, auxiliary, neutral), and $\star$ denotes the BPZ profile product. The final
forty-block seven-cycle profile of Buys–Polak–Zuiddam is $\pi_{40} = \pi_{20} \star \pi_{20}$,
where $\pi_1 = (367, 8, 367, 322)$, $\pi_2 = \pi_1 \star \pi_1$, $\pi_3 = \pi_1 \star \pi_2$,
$\pi_5 = \pi_2 \star \pi_3$, $\pi_{10} = \pi_5 \star \pi_5$ and
$\pi_{20} = \pi_{10} \star \pi_{10}$.

## Sources

- BPZ, arXiv:2607.29681, seven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi40`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi40).

## Code coordinate of the forty-block BPZ seven-cycle profile

The code coordinate (the
first of the four integer coordinates) of the forty-block seven-cycle profile $\pi_{40}$ of
Buys–Polak–Zuiddam equals
$4089635995108338053456272492117641008738901835089431264388780413340766441486608
118807897325023935704961$.

## Sources

- BPZ, arXiv:2607.29681, forty-block seven-cycle recursion.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC7Pi40_code`, a theorem declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c7-pi40-code).

## Buys–Polak–Zuiddam code for the 7-cycle in length 200

Let $c$ be the code coordinate
of BPZ's final forty-block seven-cycle profile, and let $M = \max(c, 0)$. There is a finite set
of words of length $200$ over $\mathbb{Z}/7\mathbb{Z}$ that is an independent code for the
$7$-cycle and has exactly $M$ elements.

## Sources

- BPZ, arXiv:2607.29681, the exact forty-block dimension-200 construction.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleSevenConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-seven-construction).

## Buys–Polak–Zuiddam lower bound for the capacity of the 7-cycle

Let $c$ be the code
coordinate of BPZ's final forty-block seven-cycle profile, and let $M = \max(c, 0)$. Then
$M^{1/200}$ is at most the Shannon capacity of the $7$-cycle, as an inequality in $[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, the exact dimension-200 root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleSevenLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-seven-lower-bound).

## Tandon's dimension-500 code size

Tandon's dimension-500 code size is the natural number
$M^*$ with $257$ decimal digits given by

$$
M^* = 33964672918117456943408517573718333225317390754651100605971152590324909277046876400440
35395842835926298962152039473727668119665577675838633047083277330855915999031707610213
1413374061066595834823529274560988950698158729501949866486079791784996498585401881281
$$

## Sources

- Tandon, arXiv:2608.30273, the printed Mstar value.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.tandon2026Mstar`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#tandon2026-mstar).

## Tandon's dimension-500 code for the 7-cycle

Let $M^*$ be Tandon's dimension-500 code
size. There is an independent code for the $7$-cycle consisting of words of length $500$ over
$\mathbb{Z}/7\mathbb{Z}$ with exactly $M^*$ codewords.

## Sources

- Tandon, arXiv:2608.30273, exact dimension-500 construction.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.tandon2026Construction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#tandon2026-construction).

## Tandon's lower bound for the capacity of the 7-cycle

Let $M^*$ be Tandon's
dimension-500 code size. The Shannon capacity of the $7$-cycle is at least $(M^*)^{1/500}$.

## Sources

- Tandon, arXiv:2608.30273, exact dimension-500 root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.tandon2026LowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#tandon2026-lower-bound).

## One-block BPZ profile for the 11-cycle

The one-block eleven-cycle profile of Buys,
Polak and Zuiddam is the profile with code coordinate $148$, pairs coordinate $3$, auxiliary
coordinate $148$ and neutral coordinate $142$.

In the source this profile comes from a construction in dimension $3$; that origin is not
checked here.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi1).

## Two-block BPZ profile for the 11-cycle

The two-block eleven-cycle profile of Buys,
Polak and Zuiddam is the profile product $\pi_1 \star \pi_1$, where $\pi_1$ is their one-block
eleven-cycle profile.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi2`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi2).

## Three-block BPZ profile for the 11-cycle

The three-block eleven-cycle profile of Buys,
Polak and Zuiddam is the profile product $\pi_1 \star \pi_2$, where $\pi_1$ and $\pi_2$ are
their one-block and two-block eleven-cycle profiles.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi3`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi3).

## Four-block BPZ profile for the 11-cycle

The four-block eleven-cycle profile of Buys,
Polak and Zuiddam is the profile product $\pi_2 \star \pi_2$, where $\pi_2$ is their two-block
eleven-cycle profile.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi4`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi4).

## Seven-block BPZ profile for the 11-cycle

The seven-block eleven-cycle profile of Buys,
Polak and Zuiddam is the profile product $\pi_3 \star \pi_4$, where $\pi_3$ and $\pi_4$ are
their three-block and four-block eleven-cycle profiles.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi7`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi7).

## Eight-block BPZ profile of the eleven-cycle

The eight-block BPZ profile of the
eleven-cycle is $\pi_4 \star \pi_4$, where $\pi_4$ is the four-block BPZ profile of the
eleven-cycle and $\star$ is the BPZ profile product.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi8`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi8).

## Fourteen-block BPZ profile for the 11-cycle

The fourteen-block eleven-cycle profile of
Buys, Polak and Zuiddam is the profile product $\pi_7 \star \pi_7$, where $\pi_7$ is their
seven-block eleven-cycle profile.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi14`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi14).

## Fifteen-block BPZ profile for the 11-cycle

The fifteen-block eleven-cycle profile of
Buys, Polak and Zuiddam is the profile product $\pi_7 \star \pi_8$, where $\pi_7$ and $\pi_8$
are their seven-block and eight-block eleven-cycle profiles.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi15`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi15).

## Twenty-nine-block BPZ profile for the 11-cycle

The twenty-nine-block eleven-cycle
profile of Buys, Polak and Zuiddam is the profile product $\pi_{14} \star \pi_{15}$, where
$\pi_{14}$ and $\pi_{15}$ are their fourteen-block and fifteen-block eleven-cycle profiles.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi29`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi29).

## Fifty-eight-block BPZ profile for the 11-cycle

The final fifty-eight-block eleven-cycle
profile of Buys, Polak and Zuiddam is the profile product $\pi_{29} \star \pi_{29}$, where
$\pi_{29}$ is their twenty-nine-block eleven-cycle profile.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC11Pi58`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c11-pi58).

## One-block BPZ profile of the thirteen-cycle

The one-block BPZ profile of the
thirteen-cycle is the BPZ profile with code coordinate $62530$, pairs coordinate $1014$,
auxiliary coordinate $62530$ and neutral coordinate $60502$.

BPZ describe it as their one-block six-dimensional thirteen-cycle profile.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi1).

## Two-block BPZ profile of the thirteen-cycle

The two-block BPZ profile of the
thirteen-cycle is $\pi_1 \star \pi_1$, where $\pi_1$ is the one-block BPZ profile of the
thirteen-cycle and $\star$ is the BPZ profile product.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi2`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi2).

## Three-block BPZ profile of the thirteen-cycle

The three-block BPZ profile of the
thirteen-cycle is $\pi_1 \star \pi_2$, where $\pi_1$ and $\pi_2$ are the one-block and two-block
BPZ profiles of the thirteen-cycle and $\star$ is the BPZ profile product.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi3`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi3).

## Four-block BPZ profile of the thirteen-cycle

The four-block BPZ profile of the
thirteen-cycle is $\pi_2 \star \pi_2$, where $\pi_2$ is the two-block BPZ profile of the
thirteen-cycle and $\star$ is the BPZ profile product.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi4`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi4).

## Five-block BPZ profile of the thirteen-cycle

The five-block BPZ profile of the
thirteen-cycle is $\pi_2 \star \pi_3$, where $\pi_2$ and $\pi_3$ are the two-block and three-block
BPZ profiles of the thirteen-cycle and $\star$ is the BPZ profile product.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi5`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi5).

## Nine-block BPZ profile of the thirteen-cycle

The nine-block BPZ profile of the
thirteen-cycle is $\pi_4 \star \pi_5$, where $\pi_4$ and $\pi_5$ are the four-block and five-block
BPZ profiles of the thirteen-cycle and $\star$ is the BPZ profile product.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi9`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi9).

## Seventy-two-block BPZ profile of the thirteen-cycle

Let $\pi_9$ be the nine-block BPZ
profile of the thirteen-cycle, and let $\star$ be the BPZ profile product. Set
$\sigma_0 = \pi_9$ and $\sigma_{k+1} = \sigma_k \star \sigma_k$. The seventy-two-block BPZ profile
of the thirteen-cycle is $\sigma_3$, the result of squaring $\pi_9$ three times.

This is the final profile of BPZ's thirteen-cycle construction.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC13Pi72`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c13-pi72).

## One-block BPZ profile of the fifteen-cycle

The one-block BPZ profile of the
fifteen-cycle is the BPZ profile with code coordinate $2842$, pairs coordinate $3$, auxiliary
coordinate $2842$ and neutral coordinate $2833$.

BPZ describe it as their one-block four-dimensional fifteen-cycle profile.

## Sources

- BPZ, arXiv:2607.29681, fifteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC15Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c15-pi1).

## BPZ profile of the fifteen-cycle after ten squarings

Let $\pi_1$ be the one-block BPZ
profile of the fifteen-cycle, and let $\star$ be the BPZ profile product. Set $\sigma_0 = \pi_1$
and $\sigma_{k+1} = \sigma_k \star \sigma_k$. This profile is $\sigma_{10}$, the result of
squaring $\pi_1$ ten times.

This is the final profile of BPZ's fifteen-cycle construction.

## Sources

- BPZ, arXiv:2607.29681, fifteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC15Pi1024`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c15-pi1024).

## Buys–Polak–Zuiddam one-block profile for the 19-cycle

This is the Buys–Polak–Zuiddam
(BPZ) profile whose code, pairs, auxiliary and neutral coordinates are $7666$, $2$, $7666$
and $7661$.

Only these four integers are recorded, not BPZ's four-dimensional construction behind them.

## Sources

- BPZ, arXiv:2607.29681, nineteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC19Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c19-pi1).

## Buys–Polak–Zuiddam 4096-block profile for the 19-cycle

Let $p_0$ be the one-block
19-cycle profile, whose code, pairs, auxiliary and neutral coordinates are $7666$, $2$,
$7666$ and $7661$, and let $p_{j+1} = p_j \star p_j$, where $\star$ is the
Buys–Polak–Zuiddam (BPZ) profile product. This profile is $p_{12}$, the result of squaring
$p_0$ twelve times.

## Sources

- BPZ, arXiv:2607.29681, nineteen-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC19Pi4096`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c19-pi4096).

## Buys–Polak–Zuiddam one-block profile for the 21-cycle

This is the Buys–Polak–Zuiddam
(BPZ) profile whose code, pairs, auxiliary and neutral coordinates are $11441$, $10$,
$11441$ and $11398$.

Only these four integers are recorded, not BPZ's four-dimensional construction behind them.

## Sources

- BPZ, arXiv:2607.29681, twenty-one-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC21Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c21-pi1).

## Buys–Polak–Zuiddam 1024-block profile for the 21-cycle

Let $p_0$ be the one-block
21-cycle profile, whose code, pairs, auxiliary and neutral coordinates are $11441$, $10$,
$11441$ and $11398$, and let $p_{j+1} = p_j \star p_j$, where $\star$ is the
Buys–Polak–Zuiddam (BPZ) profile product. This profile is $p_{10}$, the result of squaring
$p_0$ ten times.

## Sources

- BPZ, arXiv:2607.29681, twenty-one-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC21Pi1024`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c21-pi1024).

## Buys–Polak–Zuiddam one-block profile for the 23-cycle

This is the Buys–Polak–Zuiddam
(BPZ) profile whose code, pairs, auxiliary and neutral coordinates are $16466$, $30$,
$16466$ and $16323$.

Only these four integers are recorded, not BPZ's four-dimensional construction behind them.

## Sources

- BPZ, arXiv:2607.29681, twenty-three-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC23Pi1`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c23-pi1).

## Buys–Polak–Zuiddam 512-block profile for the 23-cycle

Let $p_0$ be the one-block
23-cycle profile, whose code, pairs, auxiliary and neutral coordinates are $16466$, $30$,
$16466$ and $16323$, and let $p_{j+1} = p_j \star p_j$, where $\star$ is the
Buys–Polak–Zuiddam (BPZ) profile product. This profile is $p_9$, the result of squaring
$p_0$ nine times.

## Sources

- BPZ, arXiv:2607.29681, twenty-three-cycle construction.

Formalized by `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpzC23Pi512`, a definition declared in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz-c23-pi512).

## Buys–Polak–Zuiddam code for the eleven-cycle in dimension 174

Let $c$ be the code
coordinate of the fifty-eight-block eleven-cycle profile $\pi_{58}$ of Buys–Polak–Zuiddam. There
is a finite set of words of length $174$ over $\mathbb{Z}/11\mathbb{Z}$ that is an independent
code for the $11$-cycle and has exactly $\max(c, 0)$ elements.

## Sources

- BPZ, arXiv:2607.29681, eleven-cycle construction in dimension 174.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleElevenConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-eleven-construction).

## Buys–Polak–Zuiddam code for the 13-cycle in length 432

Let $c$ be the code coordinate
of BPZ's final seventy-two-block thirteen-cycle profile, and let $M = \max(c, 0)$. There is a
finite set of words of length $432$ over $\mathbb{Z}/13\mathbb{Z}$ that is an independent code
for the $13$-cycle and has exactly $M$ elements.

## Sources

- BPZ, arXiv:2607.29681, thirteen-cycle construction in dimension 432.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleThirteenConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-thirteen-construction).

## Buys–Polak–Zuiddam code for the fifteen-cycle in dimension 4096

Let $c$ be the code
coordinate of the $1024$-block fifteen-cycle profile $\pi_{1024}$ of Buys–Polak–Zuiddam. There is
a finite set of words of length $4096$ over $\mathbb{Z}/15\mathbb{Z}$ that is an independent code
for the $15$-cycle and has exactly $\max(c, 0)$ elements.

## Sources

- BPZ, arXiv:2607.29681, fifteen-cycle construction in dimension 4096.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleFifteenConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-fifteen-construction).

## Buys–Polak–Zuiddam code for the nineteen-cycle in dimension 16384

Let $c$ be the code
coordinate of the $4096$-block nineteen-cycle profile $\pi_{4096}$ of Buys–Polak–Zuiddam. There
is a finite set of words of length $16384$ over $\mathbb{Z}/19\mathbb{Z}$ that is an independent
code for the $19$-cycle and has exactly $\max(c, 0)$ elements.

## Sources

- BPZ, arXiv:2607.29681, nineteen-cycle construction in dimension 16384.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleNineteenConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-nineteen-construction).

## Buys–Polak–Zuiddam code for the 21-cycle in length 4096

Let $c$ be the code coordinate
of BPZ's final twenty-one-cycle profile after ten squarings, and let $M = \max(c, 0)$. There is
a finite set of words of length $4096$ over $\mathbb{Z}/21\mathbb{Z}$ that is an independent
code for the $21$-cycle and has exactly $M$ elements.

## Sources

- BPZ, arXiv:2607.29681, twenty-one-cycle construction in dimension 4096.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleTwentyOneConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-twenty-one-construction).

## Buys–Polak–Zuiddam code for the 23-cycle in length 2048

Let $c$ be the code coordinate
of BPZ's final twenty-three-cycle profile after nine squarings, and let $M = \max(c, 0)$. There
is a finite set of words of length $2048$ over $\mathbb{Z}/23\mathbb{Z}$ that is an independent
code for the $23$-cycle and has exactly $M$ elements.

## Sources

- BPZ, arXiv:2607.29681, twenty-three-cycle construction in dimension 2048.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleTwentyThreeConstruction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-twenty-three-construction).

## Buys–Polak–Zuiddam lower bound for the capacity of the eleven-cycle

Let $c$ be the code
coordinate of the fifty-eight-block eleven-cycle profile $\pi_{58}$ of Buys–Polak–Zuiddam. Then
$\max(c, 0)^{1/174}$ is at most the Shannon capacity of the $11$-cycle, as an inequality in
$[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, exact eleven-cycle root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleElevenLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-eleven-lower-bound).

## Buys–Polak–Zuiddam lower bound for the capacity of the 13-cycle

Let $c$ be the code
coordinate of BPZ's final seventy-two-block thirteen-cycle profile, and let $M = \max(c, 0)$.
Then $M^{1/432}$ is at most the Shannon capacity of the $13$-cycle, as an inequality in
$[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, exact thirteen-cycle root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleThirteenLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-thirteen-lower-bound).

## Buys–Polak–Zuiddam lower bound for the capacity of the fifteen-cycle

Let $c$ be the
code coordinate of the $1024$-block fifteen-cycle profile $\pi_{1024}$ of Buys–Polak–Zuiddam.
Then $\max(c, 0)^{1/4096}$ is at most the Shannon capacity of the $15$-cycle, as an inequality
in $[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, exact fifteen-cycle root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleFifteenLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-fifteen-lower-bound).

## Buys–Polak–Zuiddam lower bound for the capacity of the 19-cycle

Let $c$ be the code
coordinate of BPZ's final nineteen-cycle profile after twelve squarings, and let
$M = \max(c, 0)$. Then $M^{1/16384}$ is at most the Shannon capacity of the $19$-cycle, as an
inequality in $[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, exact nineteen-cycle root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleNineteenLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-nineteen-lower-bound).

## Buys–Polak–Zuiddam lower bound for the capacity of the 21-cycle

Let $c$ be the code
coordinate of BPZ's final twenty-one-cycle profile after ten squarings, and let
$M = \max(c, 0)$. Then $M^{1/4096}$ is at most the Shannon capacity of the $21$-cycle, as an
inequality in $[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, exact twenty-one-cycle root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleTwentyOneLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-twenty-one-lower-bound).

## Buys–Polak–Zuiddam lower bound for the capacity of the 23-cycle

Let $c$ be the code
coordinate of BPZ's final twenty-three-cycle profile after nine squarings, and let
$M = \max(c, 0)$. Then $M^{1/2048}$ is at most the Shannon capacity of the $23$-cycle, as an
inequality in $[0, \infty]$.

## Sources

- BPZ, arXiv:2607.29681, exact twenty-three-cycle root rate.

Stated but not proved: `MathlibExt.Combinatorics.Coding.CycleShannonBoundsWanted.bpz2026CycleTwentyThreeLowerBound` is written with `theorem_wanted` in [WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Coding/CycleShannonBoundsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#bpz2026-cycle-twenty-three-lower-bound).

## Strong power of a graph

Let $G$ be a simple graph with vertex set $V$ and let $k$ be a
natural number. The $k$-th strong power $G^{\boxtimes k}$ is the simple graph whose vertices are
the words $x = (x_1, \dots, x_k) \in V^k$ of length $k$, in which two words $x$ and $y$ are
adjacent (confusable) when $x \neq y$ and for every $i$ either $x_i = y_i$ or $x_i$ and $y_i$ are
adjacent in $G$.

Formalized by `MathlibExt.Combinatorics.ShannonCapacityPentagonWanted.Combinatorics.ShannonCapacityPentagon.strongPower`, a definition declared in [WantedExt/Combinatorics/ShannonCapacityPentagonWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShannonCapacityPentagonWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#strong-power).

## Shannon capacity of a graph

Let $G$ be a simple graph on a finite vertex set and let
$\theta$ be a real number. For $k \ge 1$ let $G^{\boxtimes k}$ be the $k$-th strong power of $G$
and $\alpha(G^{\boxtimes k})$ its independence number. The graph $G$ has Shannon capacity $\theta$
when $\alpha(G^{\boxtimes k})^{1/k} \to \theta$ as $k \to \infty$.

Formalized by `MathlibExt.Combinatorics.ShannonCapacityPentagonWanted.Combinatorics.ShannonCapacityPentagon.HasShannonCapacity`, a definition declared in [WantedExt/Combinatorics/ShannonCapacityPentagonWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShannonCapacityPentagonWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#has-shannon-capacity).

## Lovász's theorem: the Shannon capacity of the pentagon

The cycle graph $C_5$ on five
vertices has Shannon capacity $\sqrt{5}$: writing $\alpha(C_5^{\boxtimes k})$ for the independence
number of the $k$-th strong power of $C_5$, we have $\alpha(C_5^{\boxtimes k})^{1/k} \to \sqrt{5}$
as $k \to \infty$.

## Sources

- Knill, *Some fundamental theorems in mathematics*, §238. Problem `shannon_capacity_pentagon` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.ShannonCapacityPentagonWanted.Combinatorics.ShannonCapacityPentagon.shannon_capacity_pentagon` is written with `theorem_wanted` in [WantedExt/Combinatorics/ShannonCapacityPentagonWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ShannonCapacityPentagonWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html#shannon-capacity-pentagon).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shannon capacity of a graph](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings/shannon-capacity-of-a-graph)
