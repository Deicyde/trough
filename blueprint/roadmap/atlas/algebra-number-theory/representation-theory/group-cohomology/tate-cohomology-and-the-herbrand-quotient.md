---
declaration: section
origin: cited
lean: TateCohomology.nonempty_periodicityIso, TateCohomology.tateCohomologyCard, TateCohomology.tateHomologyCard, TateCohomology.tateHomologyCard_zero, TateCohomology.tateCohomologyCard_eq_natCast, TateCohomology.HerbrandFinite, TateCohomology.herbrandQuotient, TateCohomology.herbrandQuotient_eq
statement: formalized
proof: formalized
---

# Tate cohomology and the Herbrand quotient

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html).

## Periodicity of Tate cohomology for finite cyclic groups

Let $R$ be a commutative ring,
$G$ a finite cyclic group and $A$ a representation of $G$ over $R$. Then for every integer $n$,
the Tate cohomology groups $\hat{H}^n(G, A)$ and $\hat{H}^{n+2}(G, A)$ are isomorphic as
$R$-modules.

Formalized by `TateCohomology.nonempty_periodicityIso`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/FiniteCyclic.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/FiniteCyclic.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#nonempty-periodicity-iso).

## Cardinality of Tate cohomology

Let $G$ be a finite group, $R$ a commutative ring, $M$ an
$R$-linear representation of $G$ and $n$ an integer. This is the cardinality of the Tate
cohomology group $\hat H^n(G, M)$, as a cardinal number (possibly infinite).

Formalized by `TateCohomology.tateCohomologyCard`, a definition declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#tate-cohomology-card).

## Cardinality of Tate homology

Let $G$ be a finite group, $R$ a commutative ring
and $M$ an $R$-linear representation of $G$. For an integer $n$, the cardinality $h_n(M)$
of the degree-$n$ Tate homology of $M$ is defined as the cardinal number of the Tate
cohomology group $\hat H^{-n-1}(G, M)$, following the convention $\hat H_n = \hat H^{-n-1}$.

Formalized by `TateCohomology.tateHomologyCard`, a definition declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#tate-homology-card).

## Cardinality of Tate homology in degree zero

Let $G$ be a finite group, $R$ a commutative
ring and $M$ an $R$-linear representation of $G$. The cardinality of the degree-$0$ Tate homology
of $M$ equals the cardinality of the Tate cohomology group $\hat H^{-1}(G, M)$.

The cardinality of Tate homology in degree $n$ is defined as that of $\hat H^{-n-1}(G, M)$, so
this holds by definition.

Formalized by `TateCohomology.tateHomologyCard_zero`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#tate-homology-card-zero).

## Cardinality of finite Tate cohomology as a natural number

Let $G$ be a finite group, $R$
a commutative ring, $M$ an $R$-linear representation of $G$ and $n$ an integer such that the Tate
cohomology group $\hat H^n(G, M)$ is finite. Then the cardinality of $\hat H^n(G, M)$ equals its
number of elements, a natural number viewed as a cardinal number.

Formalized by `TateCohomology.tateCohomologyCard_eq_natCast`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#tate-cohomology-card-eq-nat-cast).

## Finiteness hypothesis for the Herbrand quotient

Let $G$ be a finite group, $R$ a
commutative ring and $M$ an $R$-linear representation of $G$. The representation $M$ satisfies
the Herbrand finiteness hypothesis when its Tate cohomology groups $\hat H^0(G, M)$ and
$\hat H^{-1}(G, M)$ are both finite.

Formalized by `TateCohomology.HerbrandFinite`, a definition declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-finite).

## Herbrand quotient

Let $G$ be a finite group, $R$ a commutative ring and $M$ an
$R$-linear representation of $G$ whose Tate cohomology groups $\hat H^0(G, M)$ and
$\hat H^{-1}(G, M)$ are finite. The Herbrand quotient of $M$ is the rational number
$h(M) = |\hat H^0(G, M)| / |\hat H^{-1}(G, M)|$, where $|X|$ is the number of elements of $X$.

Formalized by `TateCohomology.herbrandQuotient`, a definition declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-quotient).

## Herbrand quotient as a ratio of orders

Let $G$ be a finite group, $R$ a commutative
ring and $M$ an $R$-linear representation of $G$ whose Tate cohomology groups $\hat H^0(G, M)$
and $\hat H^{-1}(G, M)$ are finite. Then the Herbrand quotient of $M$ equals the rational number
$|\hat H^0(G, M)| / |\hat H^{-1}(G, M)|$, where $|X|$ is the number of elements of $X$.

Formalized by `TateCohomology.herbrandQuotient_eq`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-quotient-eq).

## The denominator of the Herbrand quotient is positive

Let $G$ be a finite group, $R$ a
commutative ring and $M$ an $R$-linear representation of $G$ whose Tate cohomology groups
$\hat H^0(G, M)$ and $\hat H^{-1}(G, M)$ are finite. Then the number of elements of
$\hat H^{-1}(G, M)$ is positive.

Formalized by `TateCohomology.herbrandQuotient_den_pos`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-quotient-den-pos).

## The denominator of the Herbrand quotient is nonzero

Let $G$ be a finite group, $R$ a
commutative ring and $M$ an $R$-linear representation of $G$ whose Tate cohomology groups
$\hat H^0(G, M)$ and $\hat H^{-1}(G, M)$ are finite. Then the number of elements of
$\hat H^{-1}(G, M)$ is nonzero.

Formalized by `TateCohomology.herbrandQuotient_den_ne_zero`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-quotient-den-ne-zero).

## Positivity of the Herbrand quotient

Let $G$ be a finite group, $R$ a commutative ring
and $M$ an $R$-linear representation of $G$ whose Tate cohomology groups $\hat H^0(G, M)$ and
$\hat H^{-1}(G, M)$ are finite. Then the Herbrand quotient of $M$ is strictly positive.

Formalized by `TateCohomology.herbrandQuotient_pos`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-quotient-pos).

## Herbrand quotients agree when Tate cohomology in degrees $0$ and $-1$ is in bijection

Let $G$ be a finite group, $R$ a commutative ring and $M$, $N$ two $R$-linear representations
of $G$ whose Tate cohomology groups $\hat H^0(G, M)$, $\hat H^{-1}(G, M)$, $\hat H^0(G, N)$ and
$\hat H^{-1}(G, N)$ are finite. If there are bijections between the underlying sets of
$\hat H^0(G, M)$ and $\hat H^0(G, N)$ and between those of $\hat H^{-1}(G, M)$ and
$\hat H^{-1}(G, N)$, then the Herbrand quotients of $M$ and $N$ are equal.

Formalized by `TateCohomology.herbrandQuotient_congr`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/TateCohomology/HerbrandQuotient.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html#herbrand-quotient-congr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tate cohomology and the Herbrand quotient](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/group-cohomology/tate-cohomology-and-the-herbrand-quotient)
