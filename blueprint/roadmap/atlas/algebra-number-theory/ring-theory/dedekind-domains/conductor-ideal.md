---
declaration: section
origin: cited
lean: Subalgebra.conductorIdeal, Subalgebra.mem_conductorIdeal, Subalgebra.le_conductorIdeal_iff, Subalgebra.conductorIdeal_subset, Subalgebra.conductorIdeal_mono, Subalgebra.conductorIdeal_top, Subalgebra.conductorIdeal_eq_top_iff, Subalgebra.conductorIdeal_comap_le
statement: formalized
proof: formalized
---

# Conductor ideal

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html).

## Conductor ideal of a subalgebra

Let $R$ be a commutative semiring, $S$ a commutative
$R$-algebra and $A$ an $R$-subalgebra of $S$. The conductor ideal of $A$ is the ideal of $S$
consisting of all $s \in S$ such that $st \in A$ for every $t \in S$; it is the largest ideal of
$S$ contained in $A$.

Formalized by `Subalgebra.conductorIdeal`, a definition declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal).

## Membership in the conductor ideal

Let $R$ and $S$ be commutative semirings with $S$ an
$R$-algebra, and let $A$ be an $R$-subalgebra of $S$. An element $s \in S$ lies in the conductor
ideal of $A$ if and only if $st \in A$ for every $t \in S$.

Formalized by `Subalgebra.mem_conductorIdeal`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#mem-conductor-ideal).

## Universal property of the conductor ideal

Let $R$ and $S$ be commutative semirings with
$S$ an $R$-algebra, let $A$ be an $R$-subalgebra of $S$, and let $I$ be an ideal of $S$. Then $I$
is contained in the conductor ideal of $A$ if and only if $I$ is contained in $A$.

Formalized by `Subalgebra.le_conductorIdeal_iff`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#le-conductor-ideal-iff).

## The conductor ideal lies in the subalgebra

Let $R$ be a commutative semiring, $S$ a
commutative $R$-algebra and $A$ an $R$-subalgebra of $S$. Then the conductor ideal of $A$ is
contained in $A$.

Formalized by `Subalgebra.conductorIdeal_subset`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal-subset).

## Monotonicity of the conductor ideal

Let $R$ be a commutative semiring, $S$ a commutative
$R$-algebra and $A \subseteq B$ two $R$-subalgebras of $S$. Then the conductor ideal of $A$ is
contained in the conductor ideal of $B$.

Formalized by `Subalgebra.conductorIdeal_mono`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal-mono).

## Conductor ideal of the whole algebra

Let $R$ be a commutative semiring and $S$ a
commutative $R$-algebra. The conductor ideal of $S$, viewed as an $R$-subalgebra of itself, is
the unit ideal $S$.

Formalized by `Subalgebra.conductorIdeal_top`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal-top).

## The conductor ideal is the unit ideal only for the whole algebra

Let $R$ be a
commutative semiring, $S$ a commutative $R$-algebra and $A$ an $R$-subalgebra of $S$. The
conductor ideal of $A$ is all of $S$ if and only if $A = S$.

Formalized by `Subalgebra.conductorIdeal_eq_top_iff`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal-eq-top-iff).

## Preimage of a conductor ideal

Let $R$ be a commutative semiring, $S$ and $T$ commutative
$R$-algebras, $f \colon S \to T$ a homomorphism of $R$-algebras and $B$ an $R$-subalgebra of
$T$. Then the preimage under $f$ of the conductor ideal of $B$ is contained in the conductor
ideal of the subalgebra $f^{-1}(B)$ of $S$.

Formalized by `Subalgebra.conductorIdeal_comap_le`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal-comap-le).

## Conductor of a monogenic subalgebra

Let $R$ be a commutative ring, $S$ a commutative
$R$-algebra and $x \in S$. The conductor ideal of the subalgebra $R[x]$ of $S$ generated by $x$
equals the conductor of $x$, the ideal of all $a \in S$ such that $ab \in R[x]$ for every
$b \in S$.

Formalized by `Subalgebra.adjoin_conductorIdeal`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#adjoin-conductor-ideal).

## A finite overring has nonzero conductor

Let $R$ be an integral domain with fraction
field $K$, and let $T$ be an $R$-subalgebra of $K$ that is finitely generated as an $R$-module.
Then the conductor ideal of the image of $R$ in $T$ (the smallest $R$-subalgebra of $T$) is
nonzero.

Formalized by `Subalgebra.conductorIdeal_bot_ne_bot_of_finite`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#conductor-ideal-bot-ne-bot-of-finite).

## A subalgebra of a field with nonzero conductor is finite

Let $R$ be a Noetherian
commutative ring, $K$ a field that is an $R$-algebra, and $T$ an $R$-subalgebra of $K$. If the
conductor ideal of the image of $R$ in $T$ (the smallest $R$-subalgebra of $T$) is nonzero, then
$T$ is finitely generated as an $R$-module.

Formalized by `Subalgebra.finite_of_conductorIdeal_bot_ne_bot`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#finite-of-conductor-ideal-bot-ne-bot).

## Finiteness of an overring via its conductor

Let $R$ be a Noetherian integral domain with
fraction field $K$, and let $T$ be an $R$-subalgebra of $K$. Then the conductor ideal of the
image of $R$ in $T$ (the smallest $R$-subalgebra of $T$) is nonzero if and only if $T$ is
finitely generated as an $R$-module.

Formalized by `Subalgebra.bot_conductorIdeal_ne_bot_iff`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#bot-conductor-ideal-ne-bot-iff).

## Finiteness of the integral closure via the conductor

Let $R$ be a Noetherian integral
domain with fraction field $K$, and let $\overline{R}$ be the integral closure of $R$ in $K$,
viewed as an $R$-algebra. The conductor ideal of the smallest $R$-subalgebra of $\overline{R}$
(the image of $R$) is a nonzero ideal of $\overline{R}$ if and only if $\overline{R}$ is finitely
generated as an $R$-module.

Formalized by `Subalgebra.integralClosure_bot_conductorIdeal_ne_bot_iff`, a theorem declared in [MathlibExt/RingTheory/ConductorIdeal.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorIdeal.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#integral-closure-bot-conductor-ideal-ne).

## Residue-ring isomorphism away from a denominator-clearing ideal

Let $B$ be an algebra
over $O$, where $O$ and $B$ are commutative rings, with structure map $\varphi : O \to B$. Let
$\mathfrak q$ be a maximal ideal of $B$ and let $\mathfrak c$ be an ideal of $B$ with
$\mathfrak c \not\subseteq \mathfrak q$ such that for every $x \in \mathfrak c$ and every $b \in B$
there is $o \in O$ with $\varphi(o) = xb$. This is the ring isomorphism
$O / \varphi^{-1}(\mathfrak q) \to B / \mathfrak q$ induced by $\varphi$, which sends the class of
$o \in O$ to the class of $\varphi(o)$.

Formalized by `Ideal.quotient_coprime_residue_equiv`, a definition declared in [MathlibExt/RingTheory/ConductorResidue.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorResidue.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#quotient-coprime-residue-equiv).

## The residue-ring isomorphism on residue classes

Let $B$ be an algebra over $O$, where
$O$ and $B$ are commutative rings, with structure map $\varphi : O \to B$. Let $\mathfrak q$ be a
maximal ideal of $B$ and let $\mathfrak c$ be an ideal of $B$ with
$\mathfrak c \not\subseteq \mathfrak q$ such that for every $x \in \mathfrak c$ and every $b \in B$
there is $o \in O$ with $\varphi(o) = xb$. Then for every $o \in O$, the residue-ring isomorphism
$O / \varphi^{-1}(\mathfrak q) \cong B / \mathfrak q$ sends the class of $o$ to the class of
$\varphi(o)$.

Formalized by `Ideal.quotient_coprime_residue_equiv_apply_mk`, a theorem declared in [MathlibExt/RingTheory/ConductorResidue.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorResidue.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#quotient-coprime-residue-equiv-apply-mk).

## Equal cardinality of residue rings away from a denominator-clearing ideal

Let $B$ be an
algebra over $O$, where $O$ and $B$ are commutative rings, with structure map
$\varphi : O \to B$. Let $\mathfrak q$ be a maximal ideal of $B$ and let $\mathfrak c$ be an
ideal of $B$ with $\mathfrak c \not\subseteq \mathfrak q$ such that for every $x \in \mathfrak c$
and every $b \in B$ there is $o \in O$ with $\varphi(o) = xb$. Then
$O / \varphi^{-1}(\mathfrak q)$ and $B / \mathfrak q$ have the same cardinality, where the
cardinality of an infinite set is taken to be $0$.

Formalized by `Ideal.nat_card_quotient_coprime_residue_eq`, a theorem declared in [MathlibExt/RingTheory/ConductorResidue.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorResidue.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#nat-card-quotient-coprime-residue-eq).

## Equal ideal indices away from a denominator-clearing ideal

Let $B$ be an algebra over
$O$, where $O$ and $B$ are commutative rings, with structure map $\varphi : O \to B$. Let
$\mathfrak q$ be a maximal ideal of $B$ and let $\mathfrak c$ be an ideal of $B$ with
$\mathfrak c \not\subseteq \mathfrak q$ such that for every $x \in \mathfrak c$ and every $b \in B$
there is $o \in O$ with $\varphi(o) = xb$. Then the index of $\varphi^{-1}(\mathfrak q)$ in $O$
equals the index of $\mathfrak q$ in $B$, where the index of an ideal is the number of elements of
the quotient, taken to be $0$ when the quotient is infinite.

Formalized by `Ideal.cardQuot_coprime_residue_eq`, a theorem declared in [MathlibExt/RingTheory/ConductorResidue.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/ConductorResidue.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#card-quot-coprime-residue-eq).

## Prime ideals stay prime under denominator clearing

Let $O$ and $B$ be commutative rings,
let $B$ be an $O$-algebra whose structure map $f \colon O \to B$ is injective, let $\mathfrak p$
be a prime ideal of $O$, and let $\mathfrak c$ be an ideal of $O$ with
$\mathfrak c + \mathfrak p = O$ such that $f(x)\,b$ lies in the image of $f$ for every
$x \in \mathfrak c$ and every $b \in B$. Then the ideal $\mathfrak p B$ of $B$ generated by
$f(\mathfrak p)$ is prime.

The proof shows that the canonical map $O/\mathfrak p \to B/\mathfrak p B$ is a ring isomorphism
and transfers the integral-domain property across it.

Formalized by `Ideal.isPrime_map_of_coprime_clearDenom`, a theorem declared in [MathlibExt/RingTheory/Ideal/PrimeExtension.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeExtension.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#is-prime-map-of-coprime-clear-denom).

## Maximal ideals stay maximal under denominator clearing

Let $O$ and $B$ be commutative
rings, let $B$ be an $O$-algebra whose structure map $f \colon O \to B$ is injective, let
$\mathfrak p$ be a maximal ideal of $O$, and let $\mathfrak c$ be an ideal of $O$ with
$\mathfrak c + \mathfrak p = O$ such that $f(x)\,b$ lies in the image of $f$ for every
$x \in \mathfrak c$ and every $b \in B$. Then the ideal $\mathfrak p B$ of $B$ generated by
$f(\mathfrak p)$ is maximal.

The proof shows that the canonical map $O/\mathfrak p \to B/\mathfrak p B$ is a ring isomorphism
and transfers the field property across it.

Formalized by `Ideal.isMaximal_map_of_coprime_clearDenom`, a theorem declared in [MathlibExt/RingTheory/Ideal/PrimeExtension.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeExtension.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#is-maximal-map-of-coprime-clear-denom).

## In dimension at most one, nonzero primes extend to maximal ideals under denominator clearing

**In dimension at most one, nonzero primes extend to maximal ideals under denominator
clearing.** Let $O$ and $B$ be commutative rings such that every nonzero prime ideal of $O$ is
maximal, let $B$ be an $O$-algebra whose structure map $f \colon O \to B$ is injective, let
$\mathfrak p$ be a nonzero prime ideal of $O$, and let $\mathfrak c$ be an ideal of $O$ with
$\mathfrak c + \mathfrak p = O$ such that $f(x)\,b$ lies in the image of $f$ for every
$x \in \mathfrak c$ and every $b \in B$. Then the ideal of $B$ generated by $f(\mathfrak p)$ is
maximal.

Here dimension at most one means that every nonzero prime ideal of $O$ is maximal; for an
integral domain $O$ this is the condition that $O$ has Krull dimension at most one.

Formalized by `Ideal.isMaximal_map_of_dimensionLEOne`, a theorem declared in [MathlibExt/RingTheory/Ideal/PrimeExtension.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeExtension.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#is-maximal-map-of-dimension-leone).

## Contraction after extension fixes primes away from the conductor

Contraction after extension is the identity on primes not containing `𝔠`.

Formalized by `Ideal.comap_map_eq_of_not_le_conductor`, a lemma declared in [MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#comap-map-eq-of-not-le-conductor).

## Contraction of a nonzero ideal is nonzero

Contraction of a nonzero ideal is nonzero when `𝔠` is nonzero: a
nonzero element of `𝔠` clears a nonzero element of `𝔮` back to a nonzero
element of the contraction.

Formalized by `Ideal.comap_ne_bot_of_ne_bot`, a lemma declared in [MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#comap-ne-bot-of-ne-bot).

## Extension after contraction fixes primes away from the conductor

Extension after contraction is the identity on primes of `B` not
containing `𝔠.map f`, using that `B` has Krull dimension at most one.

Formalized by `Ideal.map_comap_eq_of_not_le_map_conductor`, a lemma declared in [MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#map-comap-eq-of-not-le-map-conductor).

## Bijection of primes away from the conductor

Contraction and extension give an equivalence between all primes of `B`
not containing `𝔠.map (algebraMap O B)` and all primes of `O` not containing
`𝔠`, including the zero prime on both sides. This restores the full spectra
in ATLAS `NumberTheoryI` Corollary 6.27.

Formalized by `Ideal.primeEquivOfNotLeConductor`, a definition declared in [MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#prime-equiv-of-not-le-conductor).

## Bijection of nonzero primes away from the conductor

Contraction and extension give an equivalence between the nonzero primes
of `B` not containing `𝔠.map (algebraMap O B)` and the nonzero primes of `O`
not containing `𝔠`. This is the restriction of
`Ideal.primeEquivOfNotLeConductor` to nonzero prime ideals.

Formalized by `Ideal.primeEquivOfCoprimeConductor`, a definition declared in [MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Ideal/PrimeBijectionConductor.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html#prime-equiv-of-coprime-conductor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conductor ideal](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/conductor-ideal/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/dedekind-domains/conductor-ideal)
