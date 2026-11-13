---
declaration: section
origin: cited
lean: MvRatFunc, PurelyTranscendental, PurelyTranscendental.exists_algEquiv_mvRatFunc, PurelyTranscendental.mvRatFunc, AlgEquiv.purelyTranscendental, AlgEquiv.purelyTranscendental', AlgebraicGeometry.purelyTranscendental_of_ringEquiv, isTranscendenceBasis_iff_algebraicIndependent_isAlgebraic
statement: formalized
proof: formalized
---

# 9.26 Transcendence

Section 9.26 of the Stacks Project, [Tag 030D](https://stacks.math.columbia.edu/tag/030D). 8 tags here are carried by 18 declarations of the repository (17 in StacksCore and 1 in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 030E, a definition

[Tag 030E](https://stacks.math.columbia.edu/tag/030E) in the Stacks Project.

**`MvRatFunc`**, an abbrev in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/MvRatFunc/Basic.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/MvRatFunc/Basic.lean#L13). The attribute's comment: “2”. References: EGA 0 (21.9.7).

> **Stacks 030E** (part 2).
> The field of multivariate rational functions in the variables indexed by `σ` over `R`,
> defined as the fraction ring of the multivariate polynomial ring `MvPolynomial σ R`.

```lean
abbrev MvRatFunc (σ R : Type*) [CommRing R] : Type _
```

**`PurelyTranscendental`**, a class in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L23). The attribute's comment: “3”. References: SGA 3 XIV (2.17); SGA 3 XIV (6.1).

> **Stacks 030E** (part 3).
> A field extension `K/k` is *purely transcendental* if there exists a set `s ⊆ K`
> that is algebraically independent over `k` and generates `K` as a field over `k`.
> Equivalently, `K` is isomorphic to the field of fractions of a polynomial ring
> over `k` on the variables indexed by `s`.

```lean
class PurelyTranscendental (k K : Type*) [Field k] [Field K] [Algebra k K] : Prop
```

**`PurelyTranscendental.exists_algEquiv_mvRatFunc`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L39). The attribute's comment: “3, a part of the correctness”.

> **Stacks 030E** (part 3, a part of the correctness).
> Any purely transcendental extension `K/k` is `k`-isomorphic to a multivariate
> field of rational functions `MvRatFunc s k` for some indexing set `s ⊆ K`.

```lean
theorem exists_algEquiv_mvRatFunc (k K : Type*) [Field k] [Field K] [Algebra k K]
    [PurelyTranscendental k K] : ∃ s : Set K, Nonempty (MvRatFunc s k ≃ₐ[k] K)
```

**`PurelyTranscendental.mvRatFunc`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L50). The attribute's comment: “3, a part of the correctness”.

> **Stacks 030E** (part 3, a part of the correctness).
> The multivariate field of rational functions `MvRatFunc σ k` is purely transcendental
> over `k`, with the variables `X i` (`i : σ`) forming a transcendence basis.

```lean
instance mvRatFunc (k σ : Type*) [Field k] : PurelyTranscendental k (MvRatFunc σ k)
```

**`AlgEquiv.purelyTranscendental`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L68). The attribute's comment: “3, a part of the correctness”.

> **Stacks 030E** (part 3, a part of the correctness).
> Pure transcendence transports across `k`-algebra isomorphisms: if `F ≃ₐ[k] E` and
> `F/k` is purely transcendental, then so is `E/k`.

```lean
theorem AlgEquiv.purelyTranscendental {k F E : Type*}
    [Field k] [Field F] [Field E] [Algebra k F] [Algebra k E]
    (e : F ≃ₐ[k] E) [PurelyTranscendental k F] : PurelyTranscendental k E
```

**`AlgEquiv.purelyTranscendental'`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L79). The attribute's comment: “3, a part of the correctness”.

> **Stacks 030E** (part 3, a part of the correctness).
> The reverse-direction transport: if `F ≃ₐ[k] E` and `E/k` is purely transcendental,
> then so is `F/k`.

```lean
theorem AlgEquiv.purelyTranscendental' {k F E : Type*}
    [Field k] [Field F] [Field E] [Algebra k F] [Algebra k E]
    (e : F ≃ₐ[k] E) [PurelyTranscendental k E] : PurelyTranscendental k F
```

**`AlgebraicGeometry.purelyTranscendental_of_ringEquiv`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/Restriction.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Devissage/Complete/Restriction.lean#L297). The attribute's comment: “3, a part of the correctness”.

> Pure transcendence transports along a pair of compatible ring isomorphisms of the base
> field and of the extension.

```lean
lemma purelyTranscendental_of_ringEquiv {k K k' K' : Type*} [Field k] [Field K] [Field k']
    [Field K'] [Algebra k K] [Algebra k' K'] (e : k ≃+* k') (E : K ≃+* K')
    (hc : (algebraMap k' K').comp e = E.toRingHom.comp (algebraMap k K))
    [PurelyTranscendental k K] : PurelyTranscendental k' K'
```

Declarations registered for the tag:

- [`isTranscendenceBasis_iff_algebraicIndependent_isAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isTranscendenceBasis_iff_algebraicIndependent_isAlgebraic#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/AlgebraicIndependent/TranscendenceBasis.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/AlgebraicIndependent/TranscendenceBasis.lean#L10) (StacksCore): “4, correctness”.

## Tag 09I8, an example

[Tag 09I8](https://stacks.math.columbia.edu/tag/09I8) in the Stacks Project.

**`transcendental_pi`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Examples/Stacks09I8.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Examples/Stacks09I8.lean#L24).

> **Stacks 09I8**.
> The real number `π` is transcendental over `ℚ`: it is not a root of any nonzero polynomial with
> rational coefficients (Lindemann, *Über die Zahl π*, Math. Ann. 20 (1882), 213–225). If it were,
> the conjugates `α` of `π i` would satisfy `∏ (1 + exp α) = 0`, contradicting the estimate
> `LindemannWeierstrass.exp_polynomial_approx`.

```lean
theorem transcendental_pi : Transcendental ℚ π
```

**`adjoinPiAlgEquivRatFunc`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Examples/Stacks09I8.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Examples/Stacks09I8.lean#L156).

> **Stacks 09I8**.
> Because `π` is transcendental over `ℚ`, the simple extension `ℚ(π)` is `ℚ`-algebra isomorphic to
> the field of rational functions `RatFunc ℚ`.

```lean
noncomputable def adjoinPiAlgEquivRatFunc : ℚ⟮π⟯ ≃ₐ[ℚ] RatFunc ℚ
```

**`purelyTranscendental_adjoinPi`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/Examples/Stacks09I8.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Examples/Stacks09I8.lean#L162).

> **Stacks 09I8**.
> The extension `ℚ(π)/ℚ` is purely transcendental, witnessed by the transcendental element `π`.

```lean
instance purelyTranscendental_adjoinPi : PurelyTranscendental ℚ ℚ⟮π⟯
```

**`Transcendental.purelyTranscendental_adjoin`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L93). The attribute's comment: “immediate generalization”.

> **Stacks 09I8** (immediate generalization).
> If `x ∈ K` is transcendental over `k`, then the simple extension `k⟮x⟯` is purely
> transcendental over `k`. The Stacks tag records the special case `Q(π)/Q`.

```lean
theorem Transcendental.purelyTranscendental_adjoin
    {k K : Type*} [Field k] [Field K] [Algebra k K] {x : K} (hx : Transcendental k x) :
    PurelyTranscendental k k⟮x⟯
```

## Tag 030F, a lemma

[Tag 030F](https://stacks.math.columbia.edu/tag/030F) in the Stacks Project.

Declarations registered for the tag:

- [`exists_isTranscendenceBasis`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exists_isTranscendenceBasis#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/AlgebraicIndependent/TranscendenceBasis.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/AlgebraicIndependent/TranscendenceBasis.lean#L11) (StacksCore): “first part”.

## Tag 09I9, an example

[Tag 09I9](https://stacks.math.columbia.edu/tag/09I9) in the Stacks Project.

**`trdeg_exp_1_pi`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Examples/Stacks09I9.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Examples/Stacks09I9.lean#L49).

> **Stacks 09I9**.
> The transcendence degree of `ℚ(e, π)` over `ℚ` is either `1` or `2`.
>
> The lower bound needs transcendence of `π`, which is `transcendental_pi` (Tag 09I8).

```lean
theorem trdeg_exp_1_pi :
    Algebra.trdeg ℚ (ℚ⟮rexp 1, π⟯) = 1 ∨ Algebra.trdeg ℚ (ℚ⟮rexp 1, π⟯) = 2
```

## Tag 09IA, an example

[Tag 09IA](https://stacks.math.columbia.edu/tag/09IA) in the Stacks Project.

**`exists_intermediateField_purelyTranscendental_and_algebraic_ne`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Examples/Stacks09IA.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Examples/Stacks09IA.lean#L22).

> **Stacks 09IA**.
> The decomposition of an extension `E/F` as a purely transcendental extension followed by an
> algebraic one is not unique. Concretely, taking `E = F(t)`, both `F(t)` and `F(t^2)` are
> intermediate fields that are purely transcendental over `F` and over which `E` is algebraic, yet
> they are distinct.

```lean
theorem exists_intermediateField_purelyTranscendental_and_algebraic_ne
    (F : Type u) [Field F] :
    ∃ (E : Type u) (_ : Field E) (_ : Algebra F E) (K L : IntermediateField F E),
    PurelyTranscendental F K ∧ Algebra.IsAlgebraic K E ∧
    PurelyTranscendental F L ∧ Algebra.IsAlgebraic L E ∧
    K ≠ L
```

**`exists_intermediateField_purelyTranscendental_and_algebraic`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyTranscendental.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyTranscendental.lean#L120).

> **Stacks 09IA**.
> Every field extension `E/F` admits an intermediate field `F'` such that `F'/F` is
> purely transcendental and `E/F'` is algebraic. (The Stacks tag also notes that this
> decomposition is not unique, e.g. for `F(t)/F` one can take either `F(t)` itself or
> `F(t²)` as the purely transcendental part.)

```lean
theorem exists_intermediateField_purelyTranscendental_and_algebraic
    (F E : Type*) [Field F] [Field E] [Algebra F E] :
    ∃ F' : IntermediateField F E, PurelyTranscendental F F' ∧ Algebra.IsAlgebraic F' E
```

## Tag 037I, a definition

[Tag 037I](https://stacks.math.columbia.edu/tag/037I) in the Stacks Project.

**`IsAlgClosedIn`**, a def in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/AlgebraicClosure.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/AlgebraicClosure.lean#L23). The attribute's comment: “2”.

> **Stacks 037I** (part 2).
> A field extension `E/F` is *algebraically closed in `E`* if every element of `E` that is
> algebraic over `F` already lies in `F`, i.e. the relative algebraic closure of `F` in `E`
> is trivial.

```lean
def IsAlgClosedIn (F E : Type*) [Field F] [Field E] [Algebra F E] : Prop
```

Declarations registered for the tag:

- [`algebraicClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=algebraicClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/AlgebraicClosure.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/AlgebraicClosure.lean#L11) (StacksCore): “(1)”. References: SGA 3 VIA (2.6.1), “(iii)”.
- [`mem_algebraicClosure_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=mem_algebraicClosure_iff#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/AlgebraicClosure.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/AlgebraicClosure.lean#L12) (StacksCore): “(1), correctness”.

## Tag 0G1M, a lemma

[Tag 0G1M](https://stacks.math.columbia.edu/tag/0G1M) in the Stacks Project.

**`MvRatFunc.rank`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/MvRatFunc/Algebra.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/MvRatFunc/Algebra.lean#L45).

> **Stacks 0G1M**.
> For an algebraic extension `S/R` of commutative rings (with `S` a domain and
> `FaithfulSMul R S`), the rank of `MvRatFunc σ S` over `MvRatFunc σ R` equals the rank of
> `S` over `R`.

```lean
theorem rank (R S σ : Type*) [CommRing R] [CommRing S]
    [IsDomain S] [Algebra R S] [Algebra.IsAlgebraic R S] [FaithfulSMul R S] :
    Module.rank (MvRatFunc σ R) (MvRatFunc σ S) = Cardinal.lift (Module.rank R S)
```

**`MvRatFunc.rank'`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/MvRatFunc/Algebra.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/MvRatFunc/Algebra.lean#L56). The attribute's comment: “universe monomorphic version”.

> **Stacks 0G1M** (universe monomorphic version).
> Same as `MvRatFunc.rank`, but with all types in the same universe, so the equality of ranks
> needs no universe lift.

```lean
theorem rank' (R : Type*) (S σ : Type u) [CommRing R] [CommRing S]
    [IsDomain S] [Algebra R S] [Algebra.IsAlgebraic R S] [FaithfulSMul R S] :
    Module.rank (MvRatFunc σ R) (MvRatFunc σ S) = Module.rank R S
```

## Tag 037J, a lemma

[Tag 037J](https://stacks.math.columbia.edu/tag/037J) in the Stacks Project.

**`finiteDimensional_algebraicClosure_of_essFiniteType`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/AlgebraicClosure.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/AlgebraicClosure.lean#L32).

> **Stacks 037J**.
> If `K/k` is an essentially finite type field extension, then the relative algebraic
> closure of `k` in `K` is finite over `k`.

```lean
instance finiteDimensional_algebraicClosure_of_essFiniteType
    (k K : Type*) [Field k] [Field K] [Algebra k K] [Algebra.EssFiniteType k K] :
    FiniteDimensional k (algebraicClosure k K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.26, Tag 030D](https://stacks.math.columbia.edu/tag/030D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
