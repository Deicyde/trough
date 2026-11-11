---
declaration: section
origin: cited
lean: AlgebraicGeometry.isRelativelyVeryAmple_and_isClosedImmersion_toProjectiveSpaceOfModule_of_separates, AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo, AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo_of_complete, AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo'
statement: formalized
proof: formalized
---

# 33.23 Separating points and tangent vectors

Section 33.23 of the Stacks Project, [Tag 0E8R](https://stacks.math.columbia.edu/tag/0E8R). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E8S, a lemma

[Tag 0E8S](https://stacks.math.columbia.edu/tag/0E8S) in the Stacks Project.

**`AlgebraicGeometry.isRelativelyVeryAmple_and_isClosedImmersion_toProjectiveSpaceOfModule_of_separates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/Canonical.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/Canonical.lean#L454).

> **[Stacks, Tag 0E8S](https://stacks.math.columbia.edu/tag/0E8S).** Let `k` be an
> algebraically closed field, let `X` be a proper `k`-scheme, let `ℒ` be an invertible
> `𝒪_X`-module and let `V ⊂ H⁰(X, ℒ)` be a `k`-subvector space. If
>
> 1. for every pair of distinct closed points `x, y ∈ X` there is a section `s ∈ V` which vanishes
>    at `x` but not at `y`, and
> 2. for every closed point `x ∈ X` and nonzero tangent vector `θ ∈ T_{X/k, x}` there exists a
>    section `s ∈ V` which vanishes at `x` but whose pullback by `θ` is nonzero,
>
> then `ℒ` is very ample and the canonical morphism `φ_{ℒ, V} : X ⟶ 𝐏(V)` is a closed immersion.
>
> The conclusion is the conjunction of four assertions: `V` is finite-dimensional over `k`; `ℒ` is
> very ample relative to the structure morphism; `V` generates `ℒ`, provided no closed point of `X`
> is its only one; and for every basis of `V` whose family of images generates `ℒ` the canonical
> morphism `φ_{ℒ, V} : X ⟶ 𝐏(V)` of [Stacks, Tag 0FCY] read in that basis is a closed immersion.
>
> Finite-dimensionality of `V` is not assumed but derived, from [Stacks, Tag 02O6] for the
> invertible module `ℒ` on the proper scheme `X`; so is generation, and so is the canonical
> morphism itself, together with the identification of the pulled-back hyperplane sheaf with `ℒ`.
> The side condition on the third assertion is the gap in the source's proof, discussed in the
> module documentation: on a scheme with exactly one closed point condition (1) is vacuous and
> `V` can generate nothing.

```lean
theorem isRelativelyVeryAmple_and_isClosedImmersion_toProjectiveSpaceOfModule_of_separates
    (p : X ⟶ Spec (.of k)) [IsProper p] (L : X.Modules) [IsInvertibleModule X L] :
    letI : Module k Γ(L, ⊤) := Module.compHom _ (baseRingMap p)
    ∀ V : Submodule k Γ(L, ⊤),
      SeparatesClosedPoints (fun v : V => (v : Γ(L, ⊤))) →
      SeparatesTangentVectors p (fun v : V => (v : Γ(L, ⊤))) →
      Module.Finite k V ∧
      Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple p L ∧
      ((∀ x : X, IsClosed ({x} : Set X) → ∃ y : X, IsClosed ({y} : Set X) ∧ y ≠ x) →
        GeneratesStalks (fun v : V => (v : Γ(L, ⊤)))) ∧
      ∀ (n : ℕ) (b : Module.Basis (Fin (n + 1)) k V)
        (hb : GeneratesStalks fun i => ((b i : V) : Γ(L, ⊤))),
        IsClosedImmersion (toProjectiveSpaceOfModule b (fun i => ((b i : V) : Γ(L, ⊤))) hb p)
```

## Tag 0E8T, a lemma

[Tag 0E8T](https://stacks.math.columbia.edu/tag/0E8T) in the Stacks Project.

**`AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/DegreeTwo.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/DegreeTwo.lean#L196). The attribute's comment: “the degree-two hypothesis is stated with the degree of a zero-dimensional subscheme as finrank over k; the classification of degree-two subschemes into point pairs and fat points is a hypothesis, as is the Tag 0FCY morphism to 𝐏(E) inherited from Tag 0E8S, and the linear system is required to be complete”.

> **[Stacks, Tag 0E8T](https://stacks.math.columbia.edu/tag/0E8T).** Let `k` be an
> algebraically closed field, let `X` be proper over `k` through `p`, let `E` be a quasi-coherent
> `k`-module and let `i : X ⟶ 𝐏(E)` be a morphism over `k` with `i^* 𝒪_{𝐏(E)}(1) ≅ ℒ` realizing the
> complete linear system of an invertible `ℒ`. If `H⁰(X, ℒ) ⟶ H⁰(Z, ℒ|_Z)` is surjective for every
> closed subscheme `Z ⊆ X` which is zero-dimensional of degree two over `k`, then `ℒ` is very ample
> relative to `p`.
>
> The two kinds of degree-two subscheme give the two separation conditions of
> [Stacks, Tag 0E8S](https://stacks.math.columbia.edu/tag/0E8S), whose very-ampleness clause then
> applies.

```lean
theorem isRelativelyVeryAmple_of_surjectsOnDegreeTwo [IsAlgClosed k]
    {E : (Spec (CommRingCat.of k)).Modules} [E.IsQuasicoherent]
    (p : X ⟶ Spec (CommRingCat.of k)) [IsProper p]
    (i : X ⟶ (relativeProj (symAlgebra E)).scheme)
    (h : i ≫ (relativeProj (symAlgebra E)).toBase = p)
    {L : X.Modules} [IsInvertibleModule X L]
    (e : (Scheme.Modules.pullback i).obj (twistOne E) ≅ L)
    {V : Type v} {t : V → (twistOne E).val.obj (op ⊤)} {ψ : V → L.val.obj (op ⊤)}
    (htψ : ∀ v, e.hom.val.app (op ⊤) (pullbackSectionTop i (twistOne E) (t v)) = ψ v)
    (hfull : Function.Surjective ψ) (hsurj : SurjectsOnDegreeTwo p L)
    (hpair : HasDegreeTwoPointPairs p L) (htan : HasDegreeTwoFatPoints p L) :
    IsRelativelyVeryAmple p L
```

**`AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo_of_complete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/DegreeTwoClassification.lean, line 646](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/DegreeTwoClassification.lean#L646). The attribute's comment: “the degree-two criterion with the classification of the degree-two zero-dimensional subschemes into point pairs and fat points PROVED; what is still assumed is the Tag 0FCY morphism to 𝐏(E) with its twist identification, inherited from Tag 0E8S, and completeness of the linear system it realizes”.

> **[Stacks, Tag 0E8T](https://stacks.math.columbia.edu/tag/0E8T), with the classification of
> the degree-two subschemes proved.** Let `k` be algebraically closed, let `X` be proper over `k`
> through `p`, let `E` be a quasi-coherent `k`-module and let `i : X ⟶ 𝐏(E)` be a morphism over
> `k` with `i^* 𝒪_{𝐏(E)}(1) ≅ ℒ` realizing the complete linear system of an invertible `ℒ`. If
> `H⁰(X, ℒ) ⟶ H⁰(Z, ℒ|_Z)` is surjective for every closed subscheme `Z ⊆ X` which is
> zero-dimensional of degree two over `k`, then `ℒ` is very ample relative to `p`.
>
> This is `AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo` with its two
> classification hypotheses supplied: `AlgebraicGeometry.hasDegreeTwoPointPairs` and
> `AlgebraicGeometry.hasDegreeTwoFatPoints`. What is still a hypothesis is the morphism to `𝐏(E)`
> with its identification of the pulled-back twist, which is the morphism of
> [Stacks, Tag 0FCY](https://stacks.math.columbia.edu/tag/0FCY) inherited from the criterion of
> [Stacks, Tag 0E8S](https://stacks.math.columbia.edu/tag/0E8S), together with completeness of the
> linear system it realizes.

```lean
theorem isRelativelyVeryAmple_of_surjectsOnDegreeTwo_of_complete
    {E : (Spec (CommRingCat.of k)).Modules} [E.IsQuasicoherent]
    (p : X ⟶ Spec (CommRingCat.of k)) [IsProper p]
    (i : X ⟶ (relativeProj (symAlgebra E)).scheme)
    (h : i ≫ (relativeProj (symAlgebra E)).toBase = p)
    {L : X.Modules} [IsInvertibleModule X L]
    (e : (Scheme.Modules.pullback i).obj (twistOne E) ≅ L)
    {V : Type v} {t : V → (twistOne E).val.obj (op ⊤)} {ψ : V → L.val.obj (op ⊤)}
    (htψ : ∀ v, e.hom.val.app (op ⊤) (pullbackSectionTop i (twistOne E) (t v)) = ψ v)
    (hfull : Function.Surjective ψ) (hsurj : SurjectsOnDegreeTwo p L) :
    IsRelativelyVeryAmple p L
```

**`AlgebraicGeometry.isRelativelyVeryAmple_of_surjectsOnDegreeTwo'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/DegreeTwoComplete.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/SeparatingPointsTangentVectors/DegreeTwoComplete.lean#L374). The attribute's comment: “the full statement, with no assumed data: the dimension of a zero-dimensional closed subscheme is the topological Krull dimension of its space and its degree is the dimension over k of its ring of global sections”.

> **[Stacks, Tag 0E8T](https://stacks.math.columbia.edu/tag/0E8T).** Let `k` be an
> algebraically closed field, let `X` be a proper `k`-scheme and let `ℒ` be an invertible
> `𝒪_X`-module. If `H⁰(X, ℒ) ⟶ H⁰(Z, ℒ|_Z)` is surjective for every closed subscheme `Z ⊆ X` of
> dimension zero and degree two over `k`, then `ℒ` is very ample on `X` over `k`.
>
> The pairs of distinct closed points and the fat points among those subschemes give the two
> separation conditions of [Stacks, Tag 0E8S](https://stacks.math.columbia.edu/tag/0E8S); the same
> hypothesis makes the global sections generate `ℒ`, so a basis of the finite-dimensional space
> `H⁰(X, ℒ)` defines a morphism to `ℙⁿ_k` realizing the complete linear system, and that morphism
> is a closed immersion. Projective space over the affine base is the projective bundle of a free
> module, which turns the immersion into the datum relative very ampleness asks for.

```lean
theorem isRelativelyVeryAmple_of_surjectsOnDegreeTwo' {k : Type u} [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} (p : X ⟶ Spec (.of k)) [IsProper p] (L : X.Modules)
    [IsInvertibleModule X L] (hsurj : SurjectsOnDegreeTwo p L) :
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple p L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.23, Tag 0E8R](https://stacks.math.columbia.edu/tag/0E8R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
