---
declaration: section
origin: cited
lean: Stacks.Curves.VeryAmpleSixthPower.isRelativelyVeryAmple_tensorPowModule_six_of_regularSection, Stacks.Curves.VeryAmpleSquare.isRelativelyVeryAmple_tensorPowModule_two
statement: formalized
proof: formalized
---

# 53.7 Very ample invertible sheaves

Section 53.7 of the Stacks Project, [Tag 0E8U](https://stacks.math.columbia.edu/tag/0E8U). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E8V, a lemma

[Tag 0E8V](https://stacks.math.columbia.edu/tag/0E8V) in the Stacks Project.

**`Stacks.Curves.VeryAmpleSixthPower.isRelativelyVeryAmple_tensorPowModule_six_of_regularSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VeryAmpleSixthPowerCriterion.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VeryAmpleSixthPowerCriterion.lean#L160).

> **[Stacks, Tag 0E8V].** Let `k` be a field, let `X` be a proper scheme over `k` of dimension
> `1` with `H⁰(X, 𝒪_X) = k`, and let `ℒ` be an invertible `𝒪_X`-module. Assume that `ℒ` has a
> regular global section, that `H¹(X, ℒ) = 0` and that `ℒ` is ample. Then `ℒ^{⊗ 6}` is very ample
> on `X` over `k`.
>
> The regular global section is a monomorphism `s : 𝒪_X ⟶ ℒ`; `H⁰(X, 𝒪_X) = k` is the hypothesis
> that the map `k ⟶ Γ(X, 𝒪_X)` is an isomorphism; very ampleness is relative very ampleness for
> `f : X ⟶ Spec k` in the sense of [Stacks, Tag 01VM].
>
> The proof is the source's. The section ring `S = Γ_*(X, ℒ)` is generated over `S₀` in degrees
> `1`, `2`, `3` (`exists_generators_le_three`, the first two paragraphs of the source), so its sixth
> Veronese subring is generated in degree one (`veroneseGeneratedInDegOne_six`), and that makes
> `ℒ^{⊗ 6}` very ample
> (`Stacks.VeroneseVeryAmple.isRelativelyVeryAmple_tensorPowModule_of_generators`,
> the source's closing sentence, which runs through `X = Proj S` of [Stacks, Tag 0C6J]).

```lean
theorem isRelativelyVeryAmple_tensorPowModule_six_of_regularSection (k : Type u) [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (L : X.Modules) [IsInvertibleModule X L] (s : 𝟙_ X.Modules ⟶ L)
    (hdim : topologicalKrullDim X = 1) (hs : Mono s)
    (hH1 : IsZero (AlgebraicGeometry.cohomologyOverField k f L 1)) (hample : IsAmple X L) :
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L (6 : ℤ))
```

## Tag 0E8W, a lemma

[Tag 0E8W](https://stacks.math.columbia.edu/tag/0E8W) in the Stacks Project.

**`Stacks.Curves.VeryAmpleSquare.isRelativelyVeryAmple_tensorPowModule_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VeryAmpleInvertibleSheaves/SquareVeryAmpleGloballyGenerated.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VeryAmpleInvertibleSheaves/SquareVeryAmpleGloballyGenerated.lean#L114).

> Let `k` be a field and `f : X ⟶ Spec k` proper with `X` of dimension `1` and
> `H⁰(X, 𝒪_X) = k`. Let `ℒ` be an invertible `𝒪_X`-module which is globally generated, has
> `H¹(X, ℒ) = 0`, and is ample. Then `ℒ^{⊗ 2}` is very ample relative to `f`.

```lean
theorem isRelativelyVeryAmple_tensorPowModule_two (k : Type u) [Field k]
    (f : X ⟶ Spec (.of k)) [IsProper f] [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (hdim : topologicalKrullDim X = 1)
    (hgg : _root_.SheafOfModules.IsGeneratedByGlobalSections L)
    (hH1 : IsZero (cohomologyOverField k f L 1)) (hample : IsAmple X L) :
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f (tensorPowModule X L 2)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.7, Tag 0E8U](https://stacks.math.columbia.edu/tag/0E8U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
