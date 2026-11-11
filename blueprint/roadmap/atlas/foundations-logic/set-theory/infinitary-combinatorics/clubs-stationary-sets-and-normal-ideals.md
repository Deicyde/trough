---
declaration: section
origin: cited
lean: MetaMathlibExt.CountableSubsets, MetaMathlibExt.IsClubOmega, MetaMathlibExt.IsStationaryOmega, MetaMathlibExt.ClosurePoints, MetaMathlibExt.ClosurePointsSeq, MetaMathlibExt.closurePointsSeq_const, MetaMathlibExt.powersetCardLT, MetaMathlibExt.IsClubPowersetCardLT
statement: formalized
proof: formalized
---

# Clubs, stationary sets and normal ideals

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html).

## Countable subsets of a set

[α]^ω or P_{ω₁}(α) is the set of countable subsets of α

Formalized by `MetaMathlibExt.CountableSubsets`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#countable-subsets-of-a-set).

## Club families of countable sets

Let $X$ be a set. A family $C$ of subsets of $X$ is club
in the countable subsets of $X$ when every member of $C$ is countable (finite or countably
infinite), every countable set $x \subseteq X$ is contained in some member of $C$, and for every
sequence $x_0 \subseteq x_1 \subseteq x_2 \subseteq \cdots$ of members of $C$ the union
$\bigcup_{n \in \mathbb{N}} x_n$ belongs to $C$.

Formalized by `MetaMathlibExt.IsClubOmega`, a structure declared in [MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#is-club-omega).

## Stationary families of countable sets

Let $X$ be a set. A family $S$ of subsets of $X$ is
stationary in the countable subsets of $X$ when $S$ meets every family $C$ that is club in the
countable subsets of $X$, that is, some set belongs to both $S$ and $C$.

Formalized by `MetaMathlibExt.IsStationaryOmega`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#is-stationary-omega).

## Closure points of a finitary function

Let $X$ be a set and let $F$ be a function
assigning an element of $X$ to every finite subset of $X$. The closure points of $F$ are the
countable (finite or countably infinite) sets $a \subseteq X$ such that $F(s) \in a$ for every
finite set $s \subseteq a$.

Formalized by `MetaMathlibExt.ClosurePoints`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#closure-points).

## Closure points of a sequence of finitary functions

Let $X$ be a set and let
$(F_n)_{n \in \mathbb{N}}$ be a sequence of functions, each assigning an element of $X$ to every
finite subset of $X$. The closure points of $(F_n)$ are the countable (finite or countably
infinite) sets $x \subseteq X$ such that $F_n(s) \in x$ for every $n \in \mathbb{N}$ and every
finite set $s \subseteq x$.

Formalized by `MetaMathlibExt.ClosurePointsSeq`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#closure-points-seq).

## Closure points and clubs of countable subsets

1. Let F : Finset(α) → α. Then ClosurePointsSeq(λ n : ℕ,, F) =      ClosurePoints(F).   2. For
   every finitary operation F, ∅ ∉ ClosurePoints(F).   3. Let f : ℕ → 𝒫(α) with each f(n) countable.
   Then ⋃_{n ∈ ℕ} f(n)      is countable.   4. [α]^ω is club in [α]^ω.   5. ∅ is not stationary in
   [α]^ω.   6. If S is stationary in [α]^ω then S ≠ ∅.   7.

The full informal statement is in the module documentation directly above.

Formalized by `MetaMathlibExt.closurePointsSeq_const`, a theorem declared in [MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/CountableSubsets.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#closure-points-and-clubs-of-countable-su).

## Subsets of $\lambda$ of size less than $\kappa$

P_κ(λ) := { x ⊆ λ ∣ |x| < κ }

Formalized by `MetaMathlibExt.powersetCardLT`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/PkappaLambda.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/PkappaLambda.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#subsets-of-lambda-of-size-less-than-kapp).

## Club subset of $P_\kappa(\lambda)$

C ⊆ P_κ(λ) is club iff

1. C is ⊆-cofinal: ∀ x ∈ P_κ(λ)  ∃ y ∈ C  (x ⊆ y), and
1. C is closed under unions of nonempty ⊆-directed subfamilies of size < κ: for every nonempty
   ⊆-directed D ⊆ C with |D| < κ, ⋃ D ∈ C.

Formalized by `MetaMathlibExt.IsClubPowersetCardLT`, a structure declared in [MathlibExt/SetTheory/Cardinal/Cofinality/PkappaLambda.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/PkappaLambda.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#club-subset-of-p-kappa-lambda).

## Family containing all bounded subsets of a cardinal

A set X⊆κ is *bounded in κ* if there is some
β<κ with α<β for every α∈ X; equivalently,
X⊆β for some β<κ.

A family I⊆𝒫(κ) *contains all bounded sets*
if every bounded X⊆κ belongs to I:

∀ X ⊆ κ  [
    (∃ β < κ ∀ α ∈ X, α < β)
     ⟶  X ∈ I
   ].

Formalized by `MetaMathlibExt.ContainsAllBounded`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#family-containing-all-bounded-subsets-of).

## $\kappa$-complete ideal on a cardinal

A *κ-complete ideal on κ* is a collection I ⊆ 𝒫(κ) such that:

1. ∅ ∈ I.
1. If A ∈ I and B ⊆ A, then B ∈ I.
1. κ ∉ I.
1. If λ < κ and ⟨ A_α : α < λ ⟩ is a sequence of members of I, then [ ⋃_{α < λ} A_α ∈ I. ]

Formalized by `MetaMathlibExt.IsKappaCompleteIdeal`, a structure declared in [MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#kappa-complete-ideal-on-a-cardinal).

## Normal ideal on a cardinal

Let κ be a cardinal, identified with
κ = Iio(κ.ord) = {α : Ordinal ∣ α < κ.ord},
and let I⊆𝒫(κ).

I is *normal* if it is closed under diagonal unions: for every
κ-sequence ⟨ A_ξ : ξ<κ⟩ with A_ξ∈ I,

∇_{ξ<κ} A_ξ := {α<κ ∣ ∃ ξ<α, α∈ A_ξ} ∈ I.

Formally,

∀ A : κ → 𝒫(κ),  (∀ ξ, A_ξ∈ I) →
  {α∈κ ∣ ∃ ξ∈κ, ξ<α ∧ α∈ A_ξ}∈ I.

Formalized by `MetaMathlibExt.IsNormalIdeal`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#normal-ideal-on-a-cardinal).

## Regressive functions

Let $\kappa$ be a cardinal, identified with its initial ordinal, let
$S$ be a set of ordinals less than $\kappa$, and let $f$ be a function from $S$ to the ordinals
less than $\kappa$. Then $f$ is regressive if $f(\alpha) < \alpha$ for every nonzero
$\alpha \in S$.

Formalized by `MetaMathlibExt.IsRegressive`, a definition declared in [MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/Cofinality/Stationary.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html#is-regressive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Clubs, stationary sets and normal ideals](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics/clubs-stationary-sets-and-normal-ideals)
