---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuasiCoherentDescent.DescentDatum, AlgebraicGeometry.Space.QuasiCoherentDescent.DescentDatum.Hom, AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackDatum, AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackFunctor, AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackCompare, AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackCompare_naturality, AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackCompare_datum_naturality, AlgebraicGeometry.Space.QuasiCoherentDescent.canonicalDescentDatum
statement: formalized
proof: formalized
---

# 74.3 Descent data for quasi-coherent sheaves

Section 74.3 of the Stacks Project, [Tag 04W2](https://stacks.math.columbia.edu/tag/04W2). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04W3, a definition

[Tag 04W3](https://stacks.math.columbia.edu/tag/04W3) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasiCoherentDescent.DescentDatum`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/DescentData.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/DescentData.lean#L109). The attribute's comment: “part (1)”.

> **Stacks 04W3, part (1).**  A descent datum for quasi-coherent modules relative to a family
> `(f i : Y i ⟶ X)` of algebraic spaces over `X`: a quasi-coherent module on each `Y i`, an
> isomorphism of the two inverse images on each pairwise fibre product, and the cocycle
> condition.

```lean
structure DescentDatum (Y : I → AlgebraicSpaces B S hS) (f : ∀ i, Y i ⟶ X)
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.DescentDatum.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/DescentData.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/DescentData.lean#L136). The attribute's comment: “part (2)”.

> **Stacks 04W3, part (2).**  A morphism of descent data: a family of morphisms of the
> component modules commuting with every pairwise isomorphism.

```lean
structure DescentDatum.Hom {Y : I → AlgebraicSpaces B S hS} {f : ∀ i, Y i ⟶ X}
    (D E : DescentDatum B S hS Y f)
```

## Tag 04W4, a lemma

[Tag 04W4](https://stacks.math.columbia.edu/tag/04W4) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean#L331). The attribute's comment: “part (1)”.

> **Stacks 04W4, part (1).**  The pullback of a descent datum for quasi-coherent modules along
> a morphism of families of morphisms with fixed target: the inverse images `(h₀ i)^*F (s₀ i)`,
> with the pairwise isomorphisms of the given datum pulled back to the pairwise fibre products of
> the source family.

```lean
def pullbackDatum (Φ : 𝒰.HomOver 𝒱 g)
    (D : DescentDatum B S hS 𝒱.X 𝒱.f) : DescentDatum B S hS 𝒰.X 𝒰.f
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean#L369). The attribute's comment: “part (2)”.

> **Stacks 04W4, part (2).**  Pullback of descent data along a morphism of families of
> morphisms with fixed target is a functor on the categories of descent data of Stacks 04W3.

```lean
def pullbackFunctor (Φ : 𝒰.HomOver 𝒱 g) :
    DescentDatum B S hS 𝒱.X 𝒱.f ⥤ DescentDatum B S hS 𝒰.X 𝒰.f
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackCompare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean#L382). The attribute's comment: “part (3), the comparison isomorphism”.

> **Stacks 04W4, part (3).**  For two morphisms of families with the same morphism of
> targets, the pairwise isomorphism of the given datum read on `U i` along `h₀ i` and `h₀' i` is
> an isomorphism of the `i`-th components of the two pulled-back data.

```lean
def pullbackCompare (Φ Ψ : 𝒰.HomOver 𝒱 g) (D : DescentDatum B S hS 𝒱.X 𝒱.f) (i : 𝒰.I₀) :
    (modulePullback B S hS (Φ.h₀ i)).obj (D.F (Φ.s₀ i)) ≅
      (modulePullback B S hS (Ψ.h₀ i)).obj (D.F (Ψ.s₀ i))
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackCompare_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean#L394). The attribute's comment: “part (3), compatibility of the comparison with the pairwise isomorphisms”.

> **Stacks 04W4, part (3).**  The components of `pullbackCompare` commute with the pairwise
> isomorphisms of the two pulled-back data, so that they constitute a morphism of descent data:
> two applications of the cocycle condition of the given datum on the test space `U i ×_U U j`,
> which carries four morphisms to members of `𝒱`.

```lean
theorem pullbackCompare_naturality
    (Φ Ψ : 𝒰.HomOver 𝒱 g) (D : DescentDatum B S hS 𝒱.X 𝒱.f) (i j : 𝒰.I₀) :
    (modulePullback B S hS (pairFst B S hS 𝒰.X 𝒰.f i j)).mapIso
          (pullbackCompare B S hS Φ Ψ D i) ≪≫ pullbackTransition B S hS Ψ D i j =
      pullbackTransition B S hS Φ D i j ≪≫
        (modulePullback B S hS (pairSnd B S hS 𝒰.X 𝒰.f i j)).mapIso
          (pullbackCompare B S hS Φ Ψ D j)
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackCompare_datum_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FamilyPullback.lean#L454). The attribute's comment: “part (3), naturality of the comparison in the descent datum”.

> **Stacks 04W4, part (3).**  The comparison is natural in the descent datum: it commutes
> with the components of the pulled-back morphisms, which are the components of
> `AlgebraicGeometry.Space.QuasiCoherentDescent.pullbackHom`.

```lean
theorem pullbackCompare_datum_naturality (Φ Ψ : 𝒰.HomOver 𝒱 g)
    {D E : DescentDatum B S hS 𝒱.X 𝒱.f} (a : D ⟶ E) (i : 𝒰.I₀) :
    (modulePullback B S hS (Φ.h₀ i)).map (a.app (Φ.s₀ i)) ≫
        (pullbackCompare B S hS Φ Ψ E i).hom =
      (pullbackCompare B S hS Φ Ψ D i).hom ≫
        (modulePullback B S hS (Ψ.h₀ i)).map (a.app (Ψ.s₀ i))
```

## Tag 04W5, a definition

[Tag 04W5](https://stacks.math.columbia.edu/tag/04W5) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasiCoherentDescent.canonicalDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/CanonicalDatum.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/CanonicalDatum.lean#L77). The attribute's comment: “the canonical descent datum”.

> **Stacks 04W5.**  The canonical descent datum `(M|_{Y i}, can)` of a quasi-coherent
> `𝒪_X`-module `M` relative to a family `(f i : Y i ⟶ X)`: the inverse images `(f i)^*M`, with
> the canonical comparison of the two inverse images of `M` on each pairwise fibre product.

```lean
def canonicalDescentDatum
    (Y : I → AlgebraicSpaces B S hS) (f : ∀ i, Y i ⟶ X)
    (M : Modules.{u, u} B S hS X.1 X.2) (hM : M.IsQuasicoherentOnSite) :
    DescentDatum B S hS Y f
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.trivialDescentDatum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/CanonicalDatum.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/CanonicalDatum.lean#L116). The attribute's comment: “the trivial descent datum”.

> **Stacks 04W5.**  The trivial descent datum of a quasi-coherent `𝒪_X`-module: its canonical
> descent datum relative to the one-member family `{𝟙 X}`.

```lean
def trivialDescentDatum
    (M : Modules.{u, u} B S hS X.1 X.2) (hM : M.IsQuasicoherentOnSite) :
    DescentDatum B S hS (fun _ : PUnit.{v + 1} => X) (fun _ => 𝟙 X)
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.IsEffective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/CanonicalDatum.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/CanonicalDatum.lean#L124). The attribute's comment: “effective descent datum”.

> **Stacks 04W5.**  A descent datum for quasi-coherent modules is effective when it is
> isomorphic to the canonical descent datum of a quasi-coherent module on the target.

```lean
def IsEffective
    (Y : I → AlgebraicSpaces B S hS) (f : ∀ i, Y i ⟶ X)
    (D : DescentDatum B S hS Y f) : Prop
```

## Tag 04W6, a lemma

[Tag 04W6](https://stacks.math.columbia.edu/tag/04W6) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasiCoherentDescent.isEtaleEffective_and_fullyFaithful_of_isZariskiCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/MemberPerMemberIsoDirect.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/MemberPerMemberIsoDirect.lean#L167).

> For a Zariski covering of an algebraic space, every descent datum for quasi-coherent modules is
> effective, and the canonical descent functor is fully faithful.

```lean
theorem isEtaleEffective_and_fullyFaithful_of_isZariskiCovering
    (hcov : IsZariskiCovering B S hS I (fun i => (Yi i).1) (fun i => (f i).hom)) :
    (∀ D : DescentDatum B S hS Yi f, IsEtaleEffective B S hS Yi f hf D) ∧
      (etaleCanonicalDescentFunctor B S hS Yi f hf).Full ∧
        (etaleCanonicalDescentFunctor B S hS Yi f hf).Faithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.3, Tag 04W2](https://stacks.math.columbia.edu/tag/04W2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
