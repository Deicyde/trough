---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isQuasiFiniteAt_of_localRingDimension_le_one, AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_localRingDimension_le_one, AlgebraicGeometry.Space.mem_isomorphismLocus_of_localRingDimension_eq_zero, AlgebraicGeometry.Space.mem_isomorphismLocus_of_finite_fibre_of_normal, AlgebraicGeometry.Space.mem_isomorphismLocus_of_localRingDimension_eq_one_of_normal
statement: formalized
proof: formalized
---

# 72.3 Generically finite morphisms

Section 72.3 of the Stacks Project, [Tag 0ACY](https://stacks.math.columbia.edu/tag/0ACY). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AD1, a lemma

[Tag 0AD1](https://stacks.math.columbia.edu/tag/0AD1) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiFiniteAt_of_localRingDimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteCodimensionOne.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GenericallyFiniteCodimensionOne.lean#L187).

> **Stacks Project, Tag 0AD1.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`
> which is locally of finite type, with `Y` locally Noetherian, and let `y` be a point of `|Y|`
> whose local ring has dimension at most one. Write `X⁰` for the points of `|X|` whose local
> ring has dimension zero. If one of the following holds — the transcendence degree of `x` over
> `f(x)` is zero for every `x` of `X⁰`; the same for every `x` of `X⁰` whose image specializes
> to `y`; `f` is quasi-finite at every point of `X⁰`; `f` is quasi-finite at a dense set of
> points of `|X|` — then `f` is quasi-finite at every point of `|X|` above `y`.
>
> The proof reduces to the corresponding statement for morphisms of schemes, Stacks 0AB6, which
> is `AlgebraicGeometry.quasiFiniteAt_of_target_stalk_dimension_le_one`, applied in an étale
> chart of the target.

```lean
theorem isQuasiFiniteAt_of_localRingDimension_le_one
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (y : points B S hS Y) (hy : localRingDimension B S hS y ≤ 1)
    (hgeneric :
      (∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        HasTranscendenceDegreeAt B S hS f x 0) ∨
      (∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        pointsMap B S hS X f x ⤳ y → HasTranscendenceDegreeAt B S hS f x 0) ∨
      (∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        IsQuasiFiniteAt B S hS f x) ∨
      Dense {x : points B S hS X | IsQuasiFiniteAt B S hS f x}) :
    ∀ x : points B S hS X, pointsMap B S hS X f x = y → IsQuasiFiniteAt B S hS f x
```

## Tag 0AD2, a lemma

[Tag 0AD2](https://stacks.math.columbia.edu/tag/0AD2) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_localRingDimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteNearCodimensionOnePoint.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteNearCodimensionOnePoint.lean#L69).

> **Stacks Project, Tag 0AD2.** Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over
> `S` with `Y` locally Noetherian, and let `y` be a point of `|Y|` whose local ring has dimension
> at most one. If one of the four generic quasi-finiteness conditions of Stacks 0AD1 holds, then
> `y` has an open neighbourhood `V ⊆ Y` over which the base change `f^{-1}(V) ⟶ V` is finite.

```lean
theorem exists_isOpenSubspace_isFinite_pullback_snd_of_localRingDimension_le_one
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hp : IsProper B S hS f)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (y : points B S hS Y) (hy : localRingDimension B S hS y ≤ 1)
    (hgeneric :
      (∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        HasTranscendenceDegreeAt B S hS f x 0) ∨
      (∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        pointsMap B S hS X f x ⤳ y → HasTranscendenceDegreeAt B S hS f x 0) ∨
      (∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        IsQuasiFiniteAt B S hS f x) ∨
      Dense {x : points B S hS X | IsQuasiFiniteAt B S hS f x}) :
    ∃ V : Subfunctor Y, IsOpenSubspace B S hS V ∧
      y ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
      IsFinite B S hS (pullback.snd f V.ι)
```

## Tag 0BBQ, a lemma

[Tag 0BBQ](https://stacks.math.columbia.edu/tag/0BBQ) in the Stacks Project.

**`AlgebraicGeometry.Space.mem_isomorphismLocus_of_localRingDimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperBirationalIsomorphismLocus.lean, line 646](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperBirationalIsomorphismLocus.lean#L646). The attribute's comment: “part (1): every point of codimension zero”.

> **Stacks 0BBQ, part (1).** Let `X` be a Noetherian algebraic space over `S` and let
> `f : Y ⟶ X` be a proper birational morphism with `Y` reduced. The maximal open subspace `U` of
> `X` over which `f` is an isomorphism contains every point of `|X|` of codimension `0`.
>
> By Stacks 0BBF the morphism is an isomorphism over a *dense* open subspace `V ⊆ X`, which is
> contained in `U` by maximality. A dense subset of the Noetherian point space `|X|` meets the
> nonempty open part of every irreducible component, so it meets the component of the given
> codimension-zero point, which is therefore in `V`.

```lean
theorem mem_isomorphismLocus_of_localRingDimension_eq_zero
    (x : points B S hS X) (hx : localRingDimension B S hS x = 0) :
    x ∈ Set.range (pointsMap B S hS U.toFunctor U.ι)
```

**`AlgebraicGeometry.Space.mem_isomorphismLocus_of_finite_fibre_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperBirationalIsomorphismLocus.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperBirationalIsomorphismLocus.lean#L676). The attribute's comment: “part (3): every point with finite fibre and normal local ring”.

> **Stacks 0BBQ, part (3).** With the hypotheses of part (1), the maximal open subspace over
> which `f` is an isomorphism contains every point of `|X|` whose fibre in `|Y|` is finite and
> whose local ring is normal.
>
> Stacks 0A4W, applied through Stacks 0ACK to convert the finite set-theoretic fibre into a
> finite geometric fibre, makes `f` finite over an open neighbourhood of the point, and
> `AlgebraicGeometry.Space.mem_isomorphismLocus_of_isFinite_over_neighbourhood` concludes.

```lean
theorem mem_isomorphismLocus_of_finite_fibre_of_normal
    (x : points B S hS X) (hfibre : ((pointsMap B S hS Y f) ⁻¹' {x}).Finite)
    (hNormal : HasNormalLocalRingAtPoint B S hS X hX x) :
    x ∈ Set.range (pointsMap B S hS U.toFunctor U.ι)
```

**`AlgebraicGeometry.Space.mem_isomorphismLocus_of_localRingDimension_eq_one_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperBirationalIsomorphismLocus.lean, line 694](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperBirationalIsomorphismLocus.lean#L694). The attribute's comment: “part (2): every point of codimension one with normal local ring”.

> **Stacks 0BBQ, part (2).** With the hypotheses of part (1), the maximal open subspace over
> which `f` is an isomorphism contains every point of `|X|` of codimension `1` whose local ring
> is normal.
>
> Part (1) already puts the image of every codimension-zero point of `|Y|` in `U`, which makes
> `f` quasi-finite there, so the third generic condition of Stacks 0AD2 holds and `f` is finite
> over an open neighbourhood of the given point; part (3)'s argument then concludes.

```lean
theorem mem_isomorphismLocus_of_localRingDimension_eq_one_of_normal
    (x : points B S hS X) (hx : localRingDimension B S hS x = 1)
    (hNormal : HasNormalLocalRingAtPoint B S hS X hX x) :
    x ∈ Set.range (pointsMap B S hS U.toFunctor U.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.3, Tag 0ACY](https://stacks.math.columbia.edu/tag/0ACY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
