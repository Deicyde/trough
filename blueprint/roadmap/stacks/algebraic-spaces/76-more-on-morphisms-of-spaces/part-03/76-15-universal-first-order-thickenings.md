---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsUniversalFirstOrderThickening, AlgebraicGeometry.Space.IsUniversalFirstOrderThickening', AlgebraicGeometry.Space.isUniversalFirstOrderThickening_iff_affine_lifting, AlgebraicGeometry.Space.HasRepresentableLiftingProperty, AlgebraicGeometry.Space.HasAffineLiftingProperty, AlgebraicGeometry.Space.isUniversalFirstOrderThickening_iff_representable, AlgebraicGeometry.Space.HasRepresentableLiftingProperty.hasAffineLiftingProperty, AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.comp_formallyEtale
statement: formalized
proof: formalized
---

# 76.15 Universal first order thickenings

Section 76.15 of the Stacks Project, [Tag 0601](https://stacks.math.columbia.edu/tag/0601). 16 tags here are carried by 52 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0602, an equation

[Tag 0602](https://stacks.math.columbia.edu/tag/0602) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Universal.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/Universal.lean#L67).

> **Stacks 0602.** A first-order thickening `Z ⊂ Z'` of algebraic spaces over `S`, equipped
> with a morphism `p : Z' ⟶ X`, is a *universal first-order thickening* of `Z` over `X` when
> every compatible solid diagram built from a first-order thickening `T ⊂ T'` over `X` admits a
> unique morphism `T' ⟶ Z'` restricting to the given `T ⟶ Z` and lying over `X`.

```lean
structure IsUniversalFirstOrderThickening (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Z' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.1)
    (p : Z' ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening'`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickening.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickening.lean#L223). The attribute's comment: “the universal first-order thickening property of diagram (0602)”.

> **Stacks 0602.** A first-order thickening `Z ⊆ Z'` over `X`, with structure morphism
> `p : Z' ⟶ X`, is *universal* when for every solid diagram of Stacks 0602 — a first-order
> thickening `T ⊆ T'` of algebraic spaces, a morphism `a : T ⟶ Z` and a morphism `b : T' ⟶ X`
> such that `T ⟶ T' ⟶ X` agrees with `T ⟶ Z ⊆ Z' ⟶ X` — there is a unique dotted arrow
> `T' ⟶ Z'` whose restriction to `T` is `a` and which lies over `X`.

```lean
structure IsUniversalFirstOrderThickening' {X Z' : AlgebraicSpaces B S hS}
    (Z : Subfunctor Z'.1) (p : Z' ⟶ X) : Prop
```

## Tag 0603, a lemma

[Tag 0603](https://stacks.math.columbia.edu/tag/0603) in the Stacks Project.

**`AlgebraicGeometry.Space.isUniversalFirstOrderThickening_iff_affine_lifting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalCriteria.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalCriteria.lean#L553). The attribute's comment: “equivalence of (1) and (3)”.

> **Stacks 0603, the equivalence of (1) and (3).** The universal property of a first-order
> thickening of algebraic spaces can already be checked on the diagrams of Stacks 0602 whose
> ambient test space is an affine scheme.

```lean
theorem isUniversalFirstOrderThickening_iff_affine_lifting
    {X Z' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.1) (p : Z' ⟶ X)
    (hZ : IsFirstOrderThickening B S hS Z' Z) :
    IsUniversalFirstOrderThickening B S hS Z p ↔
      ∀ {T' : AlgebraicSpaces B S hS} (_hT' : IsAffineSpace B S hS T'.1)
        (T : Subfunctor T'.1),
        IsFirstOrderThickening B S hS T' T →
        ∀ (a : T.toFunctor ⟶ Z.toFunctor) (b : T'.1 ⟶ X.1),
          T.ι ≫ b = a ≫ Z.ι ≫ p.hom →
          ∃! c : T'.1 ⟶ Z'.1, (T.ι ≫ c = a ≫ Z.ι) ∧ (c ≫ p.hom = b)
```

**`AlgebraicGeometry.Space.HasRepresentableLiftingProperty`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean#L144). The attribute's comment: “part (2), the lifting property tested on schemes”.

> The lifting property of the diagrams of Stacks 0602 whose ambient test object `T'` is a
> scheme, that is, whose underlying presheaf is representable.

```lean
def HasRepresentableLiftingProperty : Prop
```

**`AlgebraicGeometry.Space.HasAffineLiftingProperty`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean#L154). The attribute's comment: “part (3), the lifting property tested on affine schemes”.

> The lifting property of the diagrams of Stacks 0602 whose ambient test object `T'` is an
> affine scheme.

```lean
def HasAffineLiftingProperty : Prop
```

**`AlgebraicGeometry.Space.isUniversalFirstOrderThickening_iff_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean#L352). The attribute's comment: “equivalence of (1) and (2)”.

> A first-order thickening `Z ⊂ Z'` of algebraic spaces over `X` is a universal first-order
> thickening if and only if the dotted arrow of the diagram of Stacks 0602 exists and is unique for
> every test thickening `T ⊂ T'` whose ambient space `T'` is a *scheme*.

```lean
theorem isUniversalFirstOrderThickening_iff_representable
    (hZ : IsFirstOrderThickening B S hS Z' Z) :
    IsUniversalFirstOrderThickening B S hS Z p ↔
      HasRepresentableLiftingProperty B S hS Z p
```

**`AlgebraicGeometry.Space.HasRepresentableLiftingProperty.hasAffineLiftingProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningCriteria.lean#L365). The attribute's comment: “(2) implies (3)”.

> The lifting property of the diagrams of Stacks 0602 tested on schemes implies the same
> property tested on affine schemes.

```lean
theorem HasRepresentableLiftingProperty.hasAffineLiftingProperty
    (h : HasRepresentableLiftingProperty B S hS Z p) :
    HasAffineLiftingProperty B S hS Z p
```

## Tag 0604, a lemma

[Tag 0604](https://stacks.math.columbia.edu/tag/0604) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.comp_formallyEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FormallyEtale.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FormallyEtale.lean#L436).

> **Stacks 0604.** A universal first-order thickening of `Z` over an algebraic space `Y` is
> also a universal first-order thickening of `Z` over an algebraic space `X` whenever `Y ⟶ X` is
> formally étale: the structure morphism of the thickening is composed with the formally étale
> morphism, and nothing else changes.
>
> A solid diagram over `X` is first pushed through the formally étale morphism, which by
> Stacks 0611 has a unique lift against the thickening `T ⊂ T'`; that lift turns the diagram into
> a solid diagram over `Y`, where universality over `Y` applies. Uniqueness over `X` follows
> because any competing extension produces, after composition with the structure morphism, a lift
> of the pushed diagram, which the uniqueness clause of Stacks 0611 identifies with the chosen
> one.

```lean
theorem IsUniversalFirstOrderThickening.comp_formallyEtale {Z' Y X : AlgebraicSpaces B S hS}
    (Z : Subfunctor Z'.obj) (p : Z' ⟶ Y) (q : Y ⟶ X)
    (hp : IsUniversalFirstOrderThickening B S hS Z p) (hq : FormallyEtale q.hom) :
    IsUniversalFirstOrderThickening B S hS Z (p ≫ q)
```

## Tag 0605, a lemma

[Tag 0605](https://stacks.math.columbia.edu/tag/0605) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.etalePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningDescent.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningDescent.lean#L184). The attribute's comment: “part (1)”.

> **Stacks 0605, part (1).** Let `Y ⊂ Y'` be a universal first-order thickening of `Y` over an
> algebraic space `X`, with structure morphism `p : Y' ⟶ X`.  Let `g : Z' ⟶ Y'` be étale and let
> `Z ⊂ Z'` be a closed subspace whose inclusion sits in a cartesian square over the inclusion of
> `Y`, so that `Z = Y ×_{Y'} Z'`.  Then `Z ⊂ Z'` is a universal first-order thickening of `Z` over
> `X`, with structure morphism `g ≫ p`.
>
> The morphism `Z ⟶ Y` of the source appears as the top edge `a` of the cartesian square; it is
> automatically étale, being a base change of `g`.  The source produces `Z' ⟶ Y'` from the
> topological invariance of the spaces-étale site; here it is given, so no such input is needed.

```lean
theorem IsUniversalFirstOrderThickening.etalePullback {X Y' Z' : AlgebraicSpaces B S hS}
    (Y : Subfunctor Y'.obj) (p : Y' ⟶ X)
    (hY : IsUniversalFirstOrderThickening B S hS Y p)
    (g : Z' ⟶ Y') (hg : IsEtale B S hS g.hom)
    (Z : Subfunctor Z'.obj) (a : Z.toFunctor ⟶ Y.toFunctor)
    (hsq : IsPullback a Z.ι Y.ι g.hom) :
    IsUniversalFirstOrderThickening B S hS Z (g ≫ p)
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.of_surjectiveEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningDescent.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningDescent.lean#L513). The attribute's comment: “part (2)”.

> **Stacks 0605, part (2).** Let `Z ⟶ Y ⟶ X` be morphisms of algebraic spaces over `S` with
> `a₀ : Z ⟶ Y` surjective étale, let `g : Z' ⟶ Y'` be an étale morphism of first-order
> thickenings over `X` extending `a₀`, and let `Z ⊂ Z'` be a universal first-order thickening of
> `Z` over `X`.  Then `Y ⊂ Y'` is a universal first-order thickening of `Y` over `X`.

```lean
theorem IsUniversalFirstOrderThickening.of_surjectiveEtale
    {X Y' Z' : AlgebraicSpaces B S hS} (Y : Subfunctor Y'.obj) (Z : Subfunctor Z'.obj)
    (p : Y' ⟶ X) (g : Z' ⟶ Y') (hg : IsEtale B S hS g.hom)
    (hY : IsFirstOrderThickening B S hS Y' Y)
    (a₀ : Z.toFunctor ⟶ Y.toFunctor) (hcompat : a₀ ≫ Y.ι = Z.ι ≫ g.hom)
    (ha₀ : IsEtale B S hS a₀) (hsurj : IsSurjective B S hS a₀)
    (hZ : IsUniversalFirstOrderThickening B S hS Z (g ≫ p)) :
    IsUniversalFirstOrderThickening B S hS Y p
```

## Tag 0606, a lemma

[Tag 0606](https://stacks.math.columbia.edu/tag/0606) in the Stacks Project.

**`AlgebraicGeometry.Space.nonempty_universalFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalExistence/ExistenceAndTransport.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalExistence/ExistenceAndTransport.lean#L348).

> **Stacks 0606.** Every formally unramified morphism `h : Z ⟶ X` of algebraic spaces over
> `S` admits a universal first order thickening `Z ⊂ Z'` of `Z` over `X`, in the sense of
> Stacks 0602.

```lean
theorem nonempty_universalFirstOrderThickening
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {Z X : AlgebraicGeometry.AlgebraicSpaces B S hS} (h : Z ⟶ X)
    (hh : FormallyUnramified h.hom) :
    Nonempty (UniversalFirstOrderThickening B S hS h)
```

## Tag 0607, a definition

[Tag 0607](https://stacks.math.columbia.edu/tag/0607) in the Stacks Project.

**`AlgebraicGeometry.Space.UniversalFirstOrderThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningOfFormallyUnramified.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningOfFormallyUnramified.lean#L312). The attribute's comment: “the universal first order thickening”.

> **Stacks 0607, part (1).**  A *universal first order thickening* of a formally unramified
> morphism `h : Z ⟶ X` of algebraic spaces over `S`: the thickening `Z ⊂ Z'` of `Z` over `X` whose
> existence is Stacks 0606, presented as the datum it consists of.
>
> The ambient algebraic space is `ambient`, written `Z'` in the source, with structure morphism
> `toBase : Z' ⟶ X`; the smaller space is the closed subspace `sub` of `Z'`, which `sourceIso`
> identifies with `Z` compatibly with `h`; and `isUniversal` is the universal property of
> Stacks 0602 for that thickening over `X`.
>
> Stacks 0606, the existence of such a datum for every formally unramified `h`, is
> `AlgebraicGeometry.Space.nonempty_universalFirstOrderThickening`; it concludes `Nonempty` of this
> structure, so the datum is taken as given rather than chosen out of an existence statement, and
> the uniqueness clause of `isUniversal` is what licenses the source's definite article.

```lean
structure UniversalFirstOrderThickening {Z X : AlgebraicSpaces B S hS} (h : Z ⟶ X)
```

**`AlgebraicGeometry.Space.conormalSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningOfFormallyUnramified.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningOfFormallyUnramified.lean#L364). The attribute's comment: “the conormal sheaf”.

> **Stacks 0607, part (2).**  The *conormal sheaf* `𝒞_{Z/X}` of a formally unramified
> morphism `h : Z ⟶ X` of algebraic spaces over `S`, relative to a universal first order
> thickening `Z ⊂ Z'` of `Z` over `X`: the conormal module of Stacks 04CN of the closed subspace
> `Z ⊂ Z'`, transported to `Z` along the identification of `Z` with that closed subspace.
>
> The source writes this `𝒞_{Z/X}`, the same symbol Stacks 04CN uses for the conormal sheaf of an
> immersion, which in this library is `AlgebraicGeometry.Space.conormalModule`; no notation is
> declared, following the convention of
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalModule.lean`.

```lean
noncomputable def conormalSheaf {Z X : AlgebraicSpaces B S hS} {h : Z ⟶ X}
    (t : UniversalFirstOrderThickening B S hS h) :
    Modules.{u, u} B S hS Z.obj Z.property
```

## Tag 0608, a lemma

[Tag 0608](https://stacks.math.columbia.edu/tag/0608) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Immersion.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Immersion.lean#L90). The attribute's comment: “formally unramified”.

> **The first clause of [Stacks Project, Tag 0608].**  An immersion of algebraic spaces over
> `S` is formally unramified.
>
> An immersion is a representable morphism whose every represented base change is an immersion of
> schemes, hence unramified by `AlgebraicGeometry.unramified_of_isImmersion`; a representable
> unramified morphism is formally unramified by [Stacks Project, Tag 04AL].

```lean
theorem formallyUnramified_of_isImmersion (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {Z X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (i : Z ⟶ X)
    (hi : IsImmersion B S hS i) :
    FormallyUnramified i
```

**`AlgebraicGeometry.Space.isUniversalFirstOrderThickening_infinitesimalNeighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningImmersion.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningImmersion.lean#L329). The attribute's comment: “part (2): the universal first order thickening is the neighbourhood”.

> Let `Z` be a closed subspace of an open subspace `U` of an algebraic space `X` over `S`, so
> that `Z` is immersed in `X`, and let `N` be the first order infinitesimal neighbourhood of `Z` in
> `X`, that is the closed subspace of `U` whose kernel ideal sheaf is on every étale chart the
> square of that of `Z`.  Then `Z ⊂ N` over `X` is a universal first order thickening of `Z` over
> `X` in the sense of Stacks 0602.
>
> The universal property determines the thickening up to a unique isomorphism, so this is the
> assertion of the source that *the* universal first order thickening of `Z` over `X` is the first
> order infinitesimal neighbourhood of `Z` in `X`.
>
> The structure morphism to `X` is the inclusion of `N` in `U` followed by the inclusion of `U` in
> `X`, and `Z` is read inside `N` as the inverse image of `Z` along the former.

```lean
theorem isUniversalFirstOrderThickening_infinitesimalNeighbourhood
    (hU : IsOpenSubspace B S hS U)
    (Z N : ClosedSubspaces B S hS (⟨U.toFunctor, hU.1⟩ : AlgebraicSpaces B S hS).1)
    (hN : ∀ V : SmallEtale B S hS U.toFunctor,
      ((BigFppfOver.toScheme B S hS).map (N.2.2.rep.snd V.1.hom)).ker =
        ((BigFppfOver.toScheme B S hS).map (Z.2.2.rep.snd V.1.hom)).ker ^ 2) :
    IsUniversalFirstOrderThickening B S hS (Z.1.preimage N.1.ι)
      (ObjectProperty.homMk (N.1.ι ≫ U.ι) :
        (⟨N.1.toFunctor, N.2.1⟩ : AlgebraicSpaces B S hS) ⟶ X)
```

**`AlgebraicGeometry.Space.conormalSheafIsoConormalModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningImmersionConormal.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningImmersionConormal.lean#L257). The attribute's comment: “part (3)”.

> Let `i : Z ⟶ X` be an immersion of algebraic spaces over `S`, presented by an open subspace
> `U ⊆ X` in which `Z` is a closed subspace, and let `Z ⊂ Z'` be a universal first order thickening
> of `Z` over `X`. The conormal sheaf of `i` as a formally unramified morphism,
> [Stacks Project, Tag 0607], is isomorphic to the conormal sheaf of `i` as an immersion,
> [Stacks Project, Tag 04CN], that is to the conormal module of `Z` in `U`.

```lean
noncomputable def conormalSheafIsoConormalModule {X : AlgebraicSpaces B S hS}
    {U : Subfunctor X.1} (hU : IsOpenSubspace B S hS U)
    (Z : ClosedSubspaces B S hS (⟨U.toFunctor, hU.1⟩ : AlgebraicSpaces B S hS).1)
    (t : UniversalFirstOrderThickening B S hS
      (ObjectProperty.homMk (Z.1.ι ≫ U.ι) :
        (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS) ⟶ X)) :
    conormalSheaf B S hS t ≅ conormalModule B S hS ⟨U.toFunctor, hU.1⟩ Z
```

## Tag 0609, a lemma

[Tag 0609](https://stacks.math.columbia.edu/tag/0609) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_of_isUniversalFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningUnramified.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningUnramified.lean#L175).

> Let `Z ⊂ Z'` be a universal first order thickening of `Z` over an algebraic space `X`, with
> structure morphism `p : Z' ⟶ X`.  Then `p` is formally unramified.

```lean
theorem formallyUnramified_of_isUniversalFirstOrderThickening
    {X Z' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.1) (p : Z' ⟶ X)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p) :
    FormallyUnramified p.hom
```

**`AlgebraicGeometry.Space.UniversalFirstOrderThickening.formallyUnramified_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningUnramified.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningUnramified.lean#L198). The attribute's comment: “the universal first order thickening of a formally unramified morphism”.

> The ambient algebraic space `Z'` of a universal first order thickening of a formally
> unramified morphism `h : Z ⟶ X` of algebraic spaces over `S` is formally unramified over `X`.

```lean
theorem UniversalFirstOrderThickening.formallyUnramified_toBase
    {Z X : AlgebraicSpaces B S hS} {h : Z ⟶ X} (t : UniversalFirstOrderThickening B S hS h) :
    FormallyUnramified t.toBase.hom
```

## Tag 060A, a lemma

[Tag 060A](https://stacks.math.columbia.edu/tag/060A) in the Stacks Project.

**`AlgebraicGeometry.Space.universalThickeningMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean#L146). The attribute's comment: “the canonical morphism”.

> **Stacks 060A, the canonical morphism.** Let the square
>
> ```
>   Z --h--→ X
>   |        |
>   f        g
>   ↓        ↓
>   W --h'-→ Y
> ```
>
> of algebraic spaces over `S` commute, where `h = Z.ι ≫ p.hom` and `h' = W.ι ≫ q.hom`, let
> `Z ⊂ Z'` be a universal first-order thickening of `Z` over `X` with structure morphism `p`,
> and let `W ⊂ W'` be a universal first-order thickening of `W` over `Y` with structure morphism
> `q`.  The *canonical morphism* `f' : Z' ⟶ W'` is the dotted arrow furnished by the universal
> property of `W ⊂ W'`, applied to the first-order thickening `Z ⊂ Z'`, the morphism
> `f : Z ⟶ W` and the morphism `p ≫ g : Z' ⟶ Y`.
>
> Together with `f` it is the morphism `(f, f') : (Z, Z') ⟶ (W, W')` of thickenings over `Y` of
> the source; see `AlgebraicGeometry.Space.universalThickeningHom`.

```lean
noncomputable def universalThickeningMap (g : X ⟶ Y) (f : Z.toFunctor ⟶ W.toFunctor)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (hW : IsUniversalFirstOrderThickening B S hS W q)
    (hsq : Z.ι ≫ p.hom ≫ g.hom = f ≫ W.ι ≫ q.hom) :
    Z' ⟶ W'
```

**`AlgebraicGeometry.Space.universalThickeningMap_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean#L167). The attribute's comment: “commutativity: the canonical morphism restricts to f”.

> **Stacks 060A, commutativity: the canonical morphism restricts to `f`.** The composite
> `Z ⊂ Z' --f'--→ W'` is `Z --f--→ W ⊂ W'`.  This is the front face of the diagram of the source,
> and it says that `(f, f')` is a morphism of the thickenings.

```lean
theorem universalThickeningMap_restrict (g : X ⟶ Y) (f : Z.toFunctor ⟶ W.toFunctor)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (hW : IsUniversalFirstOrderThickening B S hS W q)
    (hsq : Z.ι ≫ p.hom ≫ g.hom = f ≫ W.ι ≫ q.hom) :
    Z.ι ≫ (universalThickeningMap B S hS g f hZ hW hsq).hom = f ≫ W.ι
```

**`AlgebraicGeometry.Space.universalThickeningMap_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean#L179). The attribute's comment: “commutativity: the canonical morphism lies over Y”.

> **Stacks 060A, commutativity: the canonical morphism is a morphism over `Y`.** The
> composite `Z' --f'--→ W' --q--→ Y` is `Z' --p--→ X --g--→ Y`.  This is the commutativity of the
> two squares of the diagram of the source which involve the base, and it says that `(f, f')` is
> a morphism of thickenings *over `Y`*.

```lean
theorem universalThickeningMap_over (g : X ⟶ Y) (f : Z.toFunctor ⟶ W.toFunctor)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (hW : IsUniversalFirstOrderThickening B S hS W q)
    (hsq : Z.ι ≫ p.hom ≫ g.hom = f ≫ W.ι ≫ q.hom) :
    universalThickeningMap B S hS g f hZ hW hsq ≫ q = p ≫ g
```

**`AlgebraicGeometry.Space.universalThickeningHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean#L210). The attribute's comment: “the canonical morphism of thickenings”.

> **Stacks 060A, the canonical morphism as a morphism of thickenings.** The pair `(f, f')`,
> read as a morphism `Arrow.mk Z.ι ⟶ Arrow.mk W.ι` of the inclusions in the arrow category: a
> packaging of the commuting square of
> `AlgebraicGeometry.Space.universalThickeningMap_restrict`.
>
> The arrow category records the square and nothing else; it is not the definition of a
> morphism of thickenings, which is Stacks 05ZK, parts (5) and (6), namely
> `AlgebraicGeometry.Space.IsMorphismOfThickenings`. That the pair is a morphism over `Y` —
> the part-(6) clause on `f'` — is `AlgebraicGeometry.Space.universalThickeningMap_over`.

```lean
noncomputable def universalThickeningHom (g : X ⟶ Y) (f : Z.toFunctor ⟶ W.toFunctor)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (hW : IsUniversalFirstOrderThickening B S hS W q)
    (hsq : Z.ι ≫ p.hom ≫ g.hom = f ≫ W.ι ≫ q.hom) :
    Arrow.mk Z.ι ⟶ Arrow.mk W.ι
```

**`AlgebraicGeometry.Space.universalThickeningConormalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningFunctorial.lean#L238). The attribute's comment: “the induced map of conormal modules”.

> **Stacks 060A, the induced map of conormal modules.** The morphism `(f, f')` of thickenings
> induces the map `f^*𝒞_{W/Y} ⟶ 𝒞_{Z/X}` of the source: it is the map of Stacks 04CP,
> `AlgebraicGeometry.Space.conormalMap`, for the square of closed immersions
>
> ```
>   Z ⊂ Z'
>   |    |
>   f    f'
>   ↓    ↓
>   W ⊂ W'
> ```
>
> whose commutativity is `AlgebraicGeometry.Space.universalThickeningMap_restrict`.
>
> By Stacks 0607 the conormal sheaf of the formally unramified `h : Z ⟶ X` is the conormal sheaf
> of `Z` in `Z'`, which is how the two spellings agree; see the implementation notes of this
> file.

```lean
noncomputable def universalThickeningConormalMap (g : X ⟶ Y) (f : Z.toFunctor ⟶ W.toFunctor)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (hW : IsUniversalFirstOrderThickening B S hS W q)
    (hsq : Z.ι ≫ p.hom ≫ g.hom = f ≫ W.ι ≫ q.hom) :
    (modulePullback B S hS (ObjectProperty.homMk f :
          (⟨Z.toFunctor, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1.1⟩ :
            AlgebraicSpaces B S hS) ⟶
          ⟨W.toFunctor, (IsNthOrderThickening.isThickening B S hS hW.firstOrder).1.1⟩)).obj
        (conormalModule B S hS W'
          ⟨W, (IsNthOrderThickening.isThickening B S hS hW.firstOrder).1⟩) ⟶
      conormalModule B S hS Z'
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩
```

## Tag 060B, a lemma

[Tag 060B](https://stacks.math.columbia.edu/tag/060B) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedBaseChange.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedBaseChange.lean#L53). The attribute's comment: “the first assertion: in a fibre product diagram, the base change `h` of a formally unramified `h'` is formally unramified”. References: EGA IV (17.1.3), “more general”.

> **Stacks 0600.** A base change of a formally unramified morphism of algebraic spaces is
> formally unramified: in a cartesian square with `f` formally unramified, the opposite side `p`
> of the square is formally unramified.
>
> This is also the first assertion of Stacks 060B: in a fibre product diagram
> `Z = X ×_Y W` of algebraic spaces over `S` with `h' : W ⟶ Y` formally unramified (here `f`),
> the morphism `h : Z ⟶ X` (here `p`) is formally unramified.

```lean
theorem formallyUnramified_of_isPullback
    {F G H P : AlgebraicSpaces B S hS}
    (f : F ⟶ G) (g : H ⟶ G) (p : P ⟶ H) (q : P ⟶ F)
    (sq : IsPullback p q g f)
    (unramified : FormallyUnramified f.hom) :
    FormallyUnramified p.hom
```

**`AlgebraicGeometry.Space.isUniversalFirstOrderThickening_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean#L250). The attribute's comment: “the second assertion: the base change of the universal first-order thickening is the universal first-order thickening of the base change”.

> **Stacks 060B, the second assertion.**  Let `W ⊂ W'` be a universal first-order thickening
> of `W` over `Y`, with structure morphism `q : W' ⟶ Y`, and let `g : X ⟶ Y` be a morphism of
> algebraic spaces.  Then `X ×_Y W ⊂ X ×_Y W'` is a universal first-order thickening of
> `X ×_Y W` over `X`, with structure morphism the projection `p : X ×_Y W' ⟶ X`.
>
> A morphism `T' ⟶ X ×_Y W'` is a pair of morphisms to `X` and to `W'` agreeing over `Y`.  Given
> a solid diagram over `X` built from a first-order thickening `T ⊂ T'` and a morphism
> `T ⟶ X ×_Y W`, the morphism to `X` is the one the diagram supplies and the morphism to `W'` is
> the unique one furnished by the universal property of `W ⊂ W'` for the diagram pushed forward
> along `X ×_Y W ⟶ W`; uniqueness of the resulting morphism is uniqueness there together with the
> mapping property of the fibre product.  That `X ×_Y W ⊆ X ×_Y W'` is a first-order thickening
> is `AlgebraicGeometry.Space.isFirstOrderThickening_baseChangeSub`, from Stacks 09ZX.

```lean
theorem isUniversalFirstOrderThickening_baseChange
    (univW : IsUniversalFirstOrderThickening B S hS W q) :
    IsUniversalFirstOrderThickening B S hS (baseChangeSub B S hS W q g)
      (baseChangeThickeningFst B S hS q g)
```

**`AlgebraicGeometry.Space.epi_universalThickeningConormalMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean#L346). The attribute's comment: “the third assertion: surjectivity of the induced map of conormal modules”.

> **Stacks 060B, the third assertion.**  The canonical map `f^*𝒞_{W/Y} ⟶ 𝒞_{Z/X}` of
> conormal modules of Stacks 060A, attached to the cartesian square of the source, is surjective.
>
> By `AlgebraicGeometry.Space.universalThickeningMap_baseChange` the morphism of ambient spaces of
> that map is the projection `r : X ×_Y W' ⟶ W'`, and the closed subspace upstairs is the inverse
> image `r⁻¹(W)`, so the map is the one of the fibre product square of
> `AlgebraicGeometry.Space.epi_conormalMap`, the surjectivity clause of Stacks 04CQ.

```lean
theorem epi_universalThickeningConormalMap_baseChange
    (univW : IsUniversalFirstOrderThickening B S hS W q) :
    Epi (universalThickeningConormalMap B S hS g
      (universalThickeningBaseChangeProjection B S hS W q g)
      (isUniversalFirstOrderThickening_baseChange B S hS W q g univW) univW
      (baseChangeThickening_square B S hS W q g))
```

## Tag 060C, a lemma

[Tag 060C](https://stacks.math.columbia.edu/tag/060C) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_baseChangeThickeningSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean#L371). The attribute's comment: “the first assertion: the induced morphism of universal first-order thickenings is flat”.

> **Stacks 060C, the first assertion.**  In the cartesian square of Stacks 060B, if `g` is flat
> then so is the induced morphism `r : X ×_Y W' ⟶ W'` of universal first-order thickenings.
>
> The projection `r` is the base change of `g` along `q : W' ⟶ Y`, and flatness of morphisms of
> algebraic spaces is stable under base change by Stacks 03MO.  That `r` is the induced morphism
> of universal first-order thickenings — the canonical morphism of Stacks 060A for this square —
> is `AlgebraicGeometry.Space.universalThickeningMap_baseChange`.
>
> Flatness is `AlgebraicGeometry.Space.IsFlat`, the chartwise flatness of Stacks 03ML part (1),
> which is the notion the source assumes of `g`.

```lean
theorem isFlat_baseChangeThickeningSnd (g_flat : IsFlat B S hS g.hom) :
    IsFlat B S hS (baseChangeThickeningSnd B S hS q g).hom
```

**`AlgebraicGeometry.Space.isIso_universalThickeningConormalMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningBaseChange.lean#L419). The attribute's comment: “the second assertion: the induced map of conormal modules is an isomorphism”.

> **Stacks 060C, the second assertion.**  In the cartesian square of Stacks 060B, if `g` is
> flat then the canonical map `f^*𝒞_{W/Y} ⟶ 𝒞_{Z/X}` of conormal modules of Stacks 060A is an
> isomorphism.
>
> Flatness of `g` is `AlgebraicGeometry.Space.IsFlat`, the chartwise flatness of Stacks 03ML
> part (1), which is the notion the source assumes.  It passes to the projection
> `r : X ×_Y W' ⟶ W'` by `AlgebraicGeometry.Space.isFlat_baseChangeThickeningSnd`, and from there
> to flatness of the induced morphism of small étale ringed topoi by Stacks 073C,
> `AlgebraicGeometry.Space.isFlat_iff_smallEtaleRingedToposHom_isFlat`, which is the hypothesis the
> flat clause of Stacks 04CQ consumes; the conclusion is then
> `AlgebraicGeometry.Space.isIso_universalThickeningConormalMap_baseChange_of_isFlatRingedTopos`.
>
> Together with `AlgebraicGeometry.Space.isFlat_baseChangeThickeningSnd` this is Stacks 060C as the
> source states it: no hypothesis beyond the configuration of Stacks 060B and flatness of `g`.

```lean
theorem isIso_universalThickeningConormalMap_baseChange
    (univW : IsUniversalFirstOrderThickening B S hS W q) (g_flat : IsFlat B S hS g.hom) :
    IsIso (universalThickeningConormalMap B S hS g
      (universalThickeningBaseChangeProjection B S hS W q g)
      (isUniversalFirstOrderThickening_baseChange B S hS W q g univW) univW
      (baseChangeThickening_square B S hS W q g))
```

## Tag 060D, a lemma

[Tag 060D](https://stacks.math.columbia.edu/tag/060D) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_of_etaleLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningDescent.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalFirstOrderThickeningDescent.lean#L490). The attribute's comment: “the étale localization of a formally unramified morphism is formally unramified”.

> **Stacks 060D, the first of its three assertions.** Let `h : Z ⟶ X` be a formally unramified
> morphism of algebraic spaces over `S`, and let `f : V ⟶ U` sit in a commutative square over it
> whose vertical arrows `v : V ⟶ Z` and `u : U ⟶ X` are étale.  Then `f` is formally unramified:
> taking the étale localization of a formally unramified morphism preserves formal unramifiedness.
>
> An étale morphism of algebraic spaces is formally étale by Stacks 0616, hence formally
> unramified, so the diagonal `v ≫ h` of the square is formally unramified by Stacks 049T.  That
> diagonal is the composite `f ≫ u`, and a first factor of a formally unramified composite whose
> second factor is formally unramified is itself formally unramified by Stacks 04G5.  Étaleness of
> `v` enters through formal unramifiedness of the diagonal and étaleness of `u` through formal
> unramifiedness of the second factor; formal unramifiedness of `h` enters through the diagonal as
> well.  The source instead reads the statement off the étale-chart criterion of Stacks 04G8; the
> route taken here proves the same statement without passing through charts.
>
> The remaining two assertions of Stacks 060D — that the universal first-order thickening of `V`
> over `U` is étale over the universal first-order thickening `Z'` of `Z` over `X`, and the
> resulting identification of conormal modules — are proved in the sibling module
> `StacksFrontier.AlgebraicGeometry.Spaces.UniversalThickeningEtaleLocalization`, which carries those
> parts of the tag; nothing in this module does.

```lean
theorem formallyUnramified_of_etaleLocalization {V U Z X : AlgebraicSpaces B S hS}
    (f : V ⟶ U) (v : V ⟶ Z) (h : Z ⟶ X) (u : U ⟶ X) (hsq : f ≫ u = v ≫ h)
    (hh : FormallyUnramified h.hom) (hv : IsEtale B S hS v.hom)
    (hu : IsEtale B S hS u.hom) :
    FormallyUnramified f.hom
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.etaleLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalization.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalization.lean#L212). The attribute's comment: “clause (2): the universal first-order thickening of the etale localization”.

> **Stacks 060D, clause (2).**  Let `Z ⊂ Z'` be a universal first-order thickening of `Z` over
> an algebraic space `X`, with structure morphism `p : Z' ⟶ X`, let `φ : U ⟶ X` be étale, let
> `g : V' ⟶ Z'` be étale with a morphism `r : V' ⟶ U` satisfying `r ≫ φ = g ≫ p`, and let
> `V ⊂ V'` be a closed subspace whose inclusion sits in a cartesian square over the inclusion of
> `Z`, so that `V = Z ×_{Z'} V'`.  Then `V ⊂ V'` is a universal first-order thickening of `V` over
> `U`, with structure morphism `r`.
>
> This says that the universal first-order thickening of `V` over `U` is the étale extension `V'`
> of `V` across `Z ⊂ Z'`, and in particular that it is étale over `Z'`, which is the assertion of
> the source.  The extension is a hypothesis rather than a conclusion of this statement, but it is
> *not* an unavailable input: the topological invariance of the spaces-étale site which produces
> it, Stacks 05ZH, is proved at a first-order thickening, and
> `Stacks.Spaces.UniversalThickening.etaleExtendsAlongFirstOrderThickening` assembles the
> extension from it unconditionally.  See the implementation notes for why the shape is kept.
>
> The morphism `V ⟶ Z` of the source appears as the top edge `c` of the cartesian square, and is
> automatically étale, being a base change of `g`.

```lean
theorem IsUniversalFirstOrderThickening.etaleLocalization
    {X U Z' V' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.obj) (p : Z' ⟶ X)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (φ : U ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (g : V' ⟶ Z') (hg : IsEtale B S hS g.hom) (r : V' ⟶ U) (hr : r ≫ φ = g ≫ p)
    (V : Subfunctor V'.obj) (c : V.toFunctor ⟶ Z.toFunctor)
    (hsq : IsPullback c V.ι Z.ι g.hom) :
    IsUniversalFirstOrderThickening B S hS V r
```

**`AlgebraicGeometry.Space.exists_isEtale_of_isUniversalFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalization.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalization.lean#L268). The attribute's comment: “clause (2): the universal first-order thickening is etale over the thickening of Z”.

> **Stacks 060D, clause (2), the étaleness assertion.**  With the data of clause (2), *every*
> universal first-order thickening `W ⊂ W'` of `V` over `U` is étale over `Z'`: there is a morphism
> `W' ⟶ Z'` which is étale, restricts on `W` to the composite `V ⟶ Z ⊂ Z'` read through the
> identification of `W` with `V`, and lies over `X`.
>
> This is the sentence of the source.  Clause (2) identifies the étale extension `V'` of `V` across
> `Z ⊂ Z'` as *a* universal first-order thickening of `V` over `U`, and the universal property of
> Stacks 0602 makes any other one isomorphic to it over `U`: the two canonical morphisms of
> Stacks 060A between them compose, in either order, to a morphism which restricts to the identity
> and lies over `U`, hence to the identity by the uniqueness clause.  Transporting the étale
> `g : V' ⟶ Z'` along that isomorphism gives the morphism asserted here.
>
> The identification of `W` with `V` is the datum `e`, with `he` saying that it is one of spaces
> over `U`; it is needed because the smaller space of a thickening is presented as a subfunctor of
> its ambient space, so two thickenings of one space never have literally the same smaller
> space.

```lean
theorem exists_isEtale_of_isUniversalFirstOrderThickening
    {X U Z' V' W' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.obj) (p : Z' ⟶ X)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (φ : U ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (g : V' ⟶ Z') (hg : IsEtale B S hS g.hom) (r : V' ⟶ U) (hr : r ≫ φ = g ≫ p)
    (V : Subfunctor V'.obj) (c : V.toFunctor ⟶ Z.toFunctor)
    (hsq : IsPullback c V.ι Z.ι g.hom)
    (W : Subfunctor W'.obj) (q : W' ⟶ U)
    (hW : IsUniversalFirstOrderThickening B S hS W q)
    (e : W.toFunctor ≅ V.toFunctor) (he : e.hom ≫ V.ι ≫ r.hom = W.ι ≫ q.hom) :
    ∃ m : W' ⟶ Z', IsEtale B S hS m.hom ∧ W.ι ≫ m.hom = e.hom ≫ V.ι ≫ g.hom ∧
      m ≫ p = q ≫ φ
```

**`AlgebraicGeometry.Space.conormalModuleEtaleLocalizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalization.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalization.lean#L322). The attribute's comment: “clause (3): the conormal module of the etale localization”.

> **Stacks 060D, clause (3).**  With the data of clause (2), the conormal module of `Z` in `Z'`
> restricts along the projection `c : V ⟶ Z` to the conormal module of `V` in `V'`:
>
> `𝒞_{Z/X}|_V = c^*𝒞_{Z/X} ≅ 𝒞_{V/U}`.
>
> The two sides are the conormal sheaves of Stacks 0607 of the formally unramified morphisms
> `Z ⟶ X` and `V ⟶ U`: the left-hand one because `Z ⊂ Z'` is a universal first-order thickening of
> `Z` over `X` by hypothesis, the right-hand one because `V ⊂ V'` is a universal first-order
> thickening of `V` over `U` by clause (2).
>
> The isomorphism is the étale base change of Stacks 04CO,
> `AlgebraicGeometry.Space.conormalModuleEtaleRestrictionIso`, for the étale morphism `g : V' ⟶ Z'`,
> transported along the cartesian square: the square forces `V` to be the inverse image `g⁻¹(Z)`
> and `c` to be the canonical projection of that inverse image.

```lean
noncomputable def conormalModuleEtaleLocalizationIso {Z' V' : AlgebraicSpaces B S hS}
    (Z : ClosedSubspaces B S hS Z'.obj) (g : V' ⟶ Z') (hg : IsEtale B S hS g.hom)
    (V : Subfunctor V'.obj) (hV : IsClosedSubspace B S hS V)
    (c : V.toFunctor ⟶ Z.1.toFunctor) (hsq : IsPullback c V.ι Z.1.ι g.hom) :
    (modulePullback B S hS
          (ObjectProperty.homMk c :
            (⟨V.toFunctor, hV.1⟩ : AlgebraicSpaces B S hS) ⟶
              (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS))).obj
        (conormalModule B S hS Z' Z) ≅
      conormalModule B S hS V' ⟨V, hV⟩
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.exists_etaleLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalizationFull.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalizationFull.lean#L137). The attribute's comment: “the thickening assertion, étale extension produced from `V ⟶ Z`, not assumed”.

> **Stacks 060D, the thickening assertion, with the étale extension produced.**  Let
> `Z ⊂ Z'` be a universal
> first-order thickening of `Z` over an algebraic space `X`, with structure morphism `p : Z' ⟶ X`,
> let `φ : U ⟶ X` be étale, and let
>
> ```
>   V ---→ U
>   |      |
>   ↓      ↓
>   Z ---→ X
> ```
>
> commute with `v : V ⟶ Z` étale.  Then there are an algebraic space `V'`, an étale
> `g : V' ⟶ Z'`, a morphism `r : V' ⟶ U` with `r ≫ φ = g ≫ p`, a subspace `V ⊂ V'` sitting in a
> cartesian square over the inclusion of `Z`, and an isomorphism of that subspace with the given
> `V` compatible with the maps to `Z` and to `U`, such that `V ⊂ V'` is a universal first-order
> thickening of `V` over `U`.
>
> Nothing about `V'` is assumed.  It is the essential-surjectivity half of the topological
> invariance of the spaces-étale site at the first-order thickening `Z ⊂ Z'`, Stacks 05ZH in the
> form `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isFirstOrderThickening`, applied to
> the object `v` of the spaces-étale site of `Z`: it returns an object of the spaces-étale site of
> `Z'` whose base change along the inclusion of `Z` is `v`.  Its subspace is the inverse image
> `g⁻¹(Z)`, which is cartesian over `Z ⊂ Z'` by Stacks 083Q,
> `CategoryTheory.Subfunctor.isPullback_preimage`, and is a first-order thickening because `g` is
> étale, by Stacks 09ZX in the étale case
> (`AlgebraicGeometry.Space.isNthOrderThickening_preimage_of_isEtale`).  The identification of
> `g⁻¹(Z)` with the given `V` is the comparison of two cartesian squares on one cospan, composed
> with the isomorphism of objects of the site.  The remaining datum, `r`, is the extension of
> `V ⟶ U` across `g⁻¹(Z) ⊂ V'`: that is the unique lift of Stacks 0611 for the formally étale
> `φ`, which is where étaleness of `φ` — rather than of `U ⟶ X` only in the source's diagram — is
> used.  That `V ⊂ V'` is then a universal first-order thickening of `V` over `U` is
> `AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.etaleLocalization`.
>
> The conormal assertion applies verbatim to the data produced here: the cartesian square returned
> below is the hypothesis of `AlgebraicGeometry.Space.conormalModuleEtaleLocalizationIso`.
>
> The attribute carries a part string rather than being bare for the reason recorded in the
> implementation notes: the first assertion of the source, formal unramifiedness of `V ⟶ U`, is
> independent of this statement — it is
> `AlgebraicGeometry.Space.formallyUnramified_of_etaleLocalization`, which takes formal
> unramifiedness of `Z ⟶ X` as a hypothesis, whereas here the universal property of Stacks 0602
> is carried instead.  The bare registration sits on
> `AlgebraicGeometry.Space.etaleLocalization_commutes_universalFirstOrderThickening` at the end of
> this file, which states all three assertions together.

```lean
theorem IsUniversalFirstOrderThickening.exists_etaleLocalization
    {X U Z' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.obj) (p : Z' ⟶ X)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (φ : U ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (V₀ : AlgebraicSpaces B S hS) (v : V₀.obj ⟶ Z.toFunctor) (hv : IsEtale B S hS v)
    (u : V₀ ⟶ U) (hcomm : u.hom ≫ φ.hom = v ≫ Z.ι ≫ p.hom) :
    ∃ (V' : AlgebraicSpaces B S hS) (g : V' ⟶ Z') (r : V' ⟶ U) (V : Subfunctor V'.obj)
      (c : V.toFunctor ⟶ Z.toFunctor) (e : V.toFunctor ≅ V₀.obj),
      IsEtale B S hS g.hom ∧ IsPullback c V.ι Z.ι g.hom ∧ r ≫ φ = g ≫ p ∧
        e.hom ≫ v = c ∧ V.ι ≫ r.hom = e.hom ≫ u.hom ∧
        IsUniversalFirstOrderThickening B S hS V r
```

**`AlgebraicGeometry.Space.etaleLocalization_commutes_universalFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalizationFull.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningEtaleLocalizationFull.lean#L251).

> **Stacks 060D.**  Taking the universal first-order thickenings commutes with étale
> localization.  Let `h : Z ⟶ X` be a formally unramified morphism of algebraic spaces over `S`,
> presented as a closed subspace `Z` of an algebraic space `Z'` with structure morphism
> `p : Z' ⟶ X`, so that `h = Z.ι ≫ p.hom`, and let `Z ⊂ Z'` be the universal first-order
> thickening of `Z` over `X`.  Let
>
> ```
>   V ---→ U
>   |      |
>   ↓      ↓
>   Z ---→ X
> ```
>
> commute with the vertical arrows `v : V ⟶ Z` and `φ : U ⟶ X` étale.  Then
>
> * `f : V ⟶ U` is formally unramified;
> * the universal first-order thickening of `V` over `U` is étale over `Z'`: there is one, and
>   *every* one admits an étale morphism to `Z'` restricting on `V` to `V ⟶ Z ⊂ Z'` and lying
>   over `X`;
> * `𝒞_{Z/X}|_V = 𝒞_{V/U}`: the *canonical* comparison map from the restriction along `V ⟶ Z` of
>   the conormal module of `Z` in `Z'` to the conormal module of `V` in that thickening — the
>   morphism underlying `AlgebraicGeometry.Space.conormalModuleEtaleLocalizationIso`, which is
>   the étale base change of Stacks 04CO transported along the cartesian square — is an
>   isomorphism.
>
> The source draws these three assertions in continuous prose and numbers none of them.
>
> The first is `AlgebraicGeometry.Space.formallyUnramified_of_etaleLocalization`.  The second is
> `AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.exists_etaleLocalization`, which
> produces the thickening `V ⊂ V'` as the étale extension of `V` across `Z ⊂ Z'`, together with
> `AlgebraicGeometry.Space.exists_isEtale_of_isUniversalFirstOrderThickening`, which carries the
> étaleness over `Z'` to any other universal first-order thickening of `V` over `U` — the source
> speaks of *the* thickening, which is determined up to unique isomorphism by Stacks 0602.  The
> third is `AlgebraicGeometry.Space.conormalModuleEtaleLocalizationIso`.
>
> The étaleness of `g` and the cartesian square are existential *binders* rather than conjuncts
> because the canonical comparison map is built from them: the third assertion then names that
> map, instead of asserting that the two conormal modules are isomorphic by some unnamed
> isomorphism.  The source writes an equality, `𝒞_{Z/X}|_V = 𝒞_{V/U}`, which is the canonical
> identification and not a bare existence claim.
>
> The smaller space of a thickening is presented as a subfunctor of its ambient space, so the
> copy of `V` inside the thickening is never literally the given `V₀`; the isomorphism `e`, and
> the identification `eW` in the second assertion, record the comparison, and the equations that
> accompany them say that it is one of spaces over `Z` and over `U`.

```lean
theorem etaleLocalization_commutes_universalFirstOrderThickening
    {X U Z' : AlgebraicSpaces B S hS} (Z : Subfunctor Z'.obj) (p : Z' ⟶ X)
    (hZ : IsUniversalFirstOrderThickening B S hS Z p)
    (hh : FormallyUnramified (Z.ι ≫ p.hom))
    (φ : U ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (V₀ : AlgebraicSpaces B S hS) (f : V₀ ⟶ U) (v : V₀.obj ⟶ Z.toFunctor)
    (hv : IsEtale B S hS v) (hcomm : f.hom ≫ φ.hom = v ≫ Z.ι ≫ p.hom) :
    FormallyUnramified f.hom ∧
      (∀ (W' : AlgebraicSpaces B S hS) (W : Subfunctor W'.obj) (q : W' ⟶ U)
          (eW : W.toFunctor ≅ V₀.obj), IsUniversalFirstOrderThickening B S hS W q →
          eW.hom ≫ f.hom = W.ι ≫ q.hom →
          ∃ m : W' ⟶ Z', IsEtale B S hS m.hom ∧
            W.ι ≫ m.hom = eW.hom ≫ v ≫ Z.ι ∧ m ≫ p = q ≫ φ) ∧
      ∃ (V' : AlgebraicSpaces B S hS) (g : V' ⟶ Z') (r : V' ⟶ U) (V : Subfunctor V'.obj)
        (c : V.toFunctor ⟶ Z.toFunctor) (e : V.toFunctor ≅ V₀.obj)
        (hV : IsUniversalFirstOrderThickening B S hS V r) (hg : IsEtale B S hS g.hom)
        (hsq : IsPullback c V.ι Z.ι g.hom),
        r ≫ φ = g ≫ p ∧ e.hom ≫ v = c ∧ V.ι ≫ r.hom = e.hom ≫ f.hom ∧
          IsIso (conormalModuleEtaleLocalizationIso B S hS ⟨Z, hZ.firstOrder.1.1⟩ g hg V
            hV.firstOrder.1.1 c hsq).hom
```

## Tag 060E, a lemma

[Tag 060E](https://stacks.math.columbia.edu/tag/060E) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_restrict_of_isSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentials.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentials.lean#L312). The attribute's comment: “granted, as `hetale`, the étale localization of 04CU and 060D: over each object of the small étale site of `Z` the restriction along `Z ⟶ Z'` of the comparison map of 04CX is, on sections, the map 04FB of a universal first-order thickening of schemes assembled from charts of `Z'`, `X` and `Y` over that object. The scheme case 04FB is applied, not granted; formal unramifiedness of `h` is not assumed, a universal first-order thickening being given”.

> **Stacks 060E.**  Let `h : Z ⟶ X` be a morphism of algebraic spaces over `S`, presented as
> the composite `Z.ι ≫ h'` of the inclusion of a closed subspace `Z` of an algebraic space `Z'`
> with a structure morphism `h' : Z' ⟶ X`, and let `Z ⊂ Z'` be a universal first-order thickening
> of `Z` over `X`.  For a morphism `p : X ⟶ Y` to a base algebraic space, the comparison map
> `c_{h'} : (h')^*Ω_{X/Y} ⟶ Ω_{Z'/Y}` of Stacks 04CX induces an isomorphism
> `h^*Ω_{X/Y} ⟶ Ω_{Z'/Y} ⊗ 𝒪_Z`, namely its restriction along the inclusion of `Z`.
>
> The map is named by the characterizing property of Stacks 04CX, which determines it uniquely by
> `AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap`; that uniqueness carries the
> étale-local input from the realization `c₀` it is stated for to the realization `c` in hand.
> The proof is the source's: over an étale chart of `Z` the restricted comparison map is the map
> of Stacks 04FB of a universal first-order thickening of schemes, which is an isomorphism, and a
> morphism of `𝒪_Z`-modules which is bijective on the sections over every chart is an
> isomorphism.
>
> Formal unramifiedness of `h`, a hypothesis of the source, is not assumed: it is what makes a
> universal first-order thickening exist, one is given, and by Stacks 0609 it follows.

```lean
theorem isIso_restrict_of_isSheafOfDifferentialsMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (c c₀ : (modulePullback B S hS h').obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS (h' ≫ p))
    (hc : IsSheafOfDifferentialsMap B S hS h' p (h' ≫ p) c)
    (hc₀ : IsSheafOfDifferentialsMap B S hS h' p (h' ≫ p) c₀)
    (hetale : IsEtaleLocalThickeningDifferentialsMap B S hS hZ p
      ((modulePullback B S hS (universalThickeningInclusion B S hS hZ)).map c₀)) :
    IsIso ((modulePullback B S hS (universalThickeningInclusion B S hS hZ)).map c)
```

**`AlgebraicGeometry.Space.isIso_thickeningSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentials.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentials.lean#L349). The attribute's comment: “granted, as `hetale`, the étale localization of 04CU and 060D, as for `isIso_restrict_of_isSheafOfDifferentialsMap`; stated for the comparison map of 04CX as constructed”.

> **Stacks 060E** for the comparison map constructed by
> `AlgebraicGeometry.Space.sheafOfDifferentialsMap`: the map
> `AlgebraicGeometry.Space.thickeningSheafOfDifferentialsMap` is an isomorphism.
>
> This is `AlgebraicGeometry.Space.isIso_restrict_of_isSheafOfDifferentialsMap` at the realization
> of the comparison map which Stacks 04CX constructs, whose characterizing property is
> `AlgebraicGeometry.Space.isSheafOfDifferentialsMap_sheafOfDifferentialsMap`.

```lean
theorem isIso_thickeningSheafOfDifferentialsMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (hetale : IsEtaleLocalThickeningDifferentialsMap B S hS hZ p
      (thickeningSheafOfDifferentialsMap B S hS hZ p)) :
    IsIso (thickeningSheafOfDifferentialsMap B S hS hZ p)
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.isIso_restrict_of_isSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentialsIso.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentialsIso.lean#L69).

> For a universal first-order thickening `Z ⊂ Z'` over `X` with structure morphism `h'`, and a
> morphism `p : X ⟶ Y`, the restriction along the inclusion `ι : Z ⟶ Z'` of any realization `c` of
> the comparison map `(h')^*Ω_{X/Y} ⟶ Ω_{Z'/Y}` is an isomorphism `h^*Ω_{X/Y} ≅ Ω_{Z'/Y} ⊗ 𝒪_Z`.

```lean
theorem isIso_restrict_of_isSheafOfDifferentialsMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    {c : (modulePullback B S hS h').obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS (h' ≫ p)}
    (hc : IsSheafOfDifferentialsMap B S hS h' p (h' ≫ p) c) :
    IsIso ((modulePullback B S hS (universalThickeningInclusion B S hS hZ)).map c)
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.isIso_thickeningSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentialsIso.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningDifferentialsIso.lean#L93).

> For a universal first-order thickening `Z ⊂ Z'` and a morphism `p : X ⟶ Y`, the comparison
> map `AlgebraicGeometry.Space.thickeningSheafOfDifferentialsMap` is an isomorphism.

```lean
theorem isIso_thickeningSheafOfDifferentialsMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y) :
    IsIso (thickeningSheafOfDifferentialsMap B S hS hZ p)
```

## Tag 060F, a lemma

[Tag 060F](https://stacks.math.columbia.edu/tag/060F) in the Stacks Project.

**`AlgebraicGeometry.Space.thickeningConormalFirstMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean#L180). The attribute's comment: “the canonical first arrow `𝒞_{Z/X} ⟶ h^*Ω_{X/Y}`, with `𝒞_{Z/X}` the conormal module of `Z ⊂ Z'` of 0607(2) and the middle term read as `ι^*(h')^*Ω_{X/Y}`; granted as `he` that the map of 060E is an isomorphism, which `isIso_thickeningSheafOfDifferentialsMap` supplies”.

> **Stacks 060F, the canonical first arrow** `𝒞_{Z/X} ⟶ h^*Ω_{X/Y}`.
>
> The source `𝒞_{Z/X}` is the conormal module `𝒞_{Z/Z'}` of the closed subspace `Z ⊂ Z'`, which is
> what Stacks 0607, part (2) defines `𝒞_{Z/X}` to be; the target `h^*Ω_{X/Y}` is read as the double
> inverse image `ι^*(h')^*Ω_{X/Y}`, as in Stacks 060E.  The arrow is the first arrow
> `AlgebraicGeometry.Space.conormalSequenceFirstMap` of Stacks 05ZA for `Z ⊂ Z'` over `Y`, followed
> by the inverse of the isomorphism `AlgebraicGeometry.Space.thickeningSheafOfDifferentialsMap` of
> Stacks 060E.
>
> The hypothesis `he` is that isomorphism, which
> `AlgebraicGeometry.Space.isIso_thickeningSheafOfDifferentialsMap` supplies.

```lean
noncomputable def thickeningConormalFirstMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (he : IsIso (thickeningSheafOfDifferentialsMap B S hS hZ p)) :
    conormalModule B S hS Z' (thickeningClosedSubspace B S hS hZ) ⟶
      (modulePullback B S hS (universalThickeningInclusion B S hS hZ)).obj
        ((modulePullback B S hS h').obj (sheafOfDifferentials B S hS p))
```

**`AlgebraicGeometry.Space.thickeningConormalFirstMap_comp_thickeningSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean#L227). The attribute's comment: “the first arrow is induced by `d_{Z'/B}`: composed with the isomorphism of 060E it is the first arrow of 05ZA for `Z ⊂ Z'` over the base, which `conormalSequenceIdealDifferential_val_app_apply` identifies with `d_{Z'/B}` on the defining ideal sheaf; granted as `he` that the map of 060E is an isomorphism”.

> **Stacks 060F, "the first arrow is induced by `d_{Z'/Y}`".**  Composed with the isomorphism
> of Stacks 060E, the first arrow is the first arrow of Stacks 05ZA for the closed subspace
> `Z ⊂ Z'` over `Y`; and that arrow is induced by `d_{Z'/Y}` in the sense of
> `AlgebraicGeometry.Space.conormalSequenceIdealDifferential_val_app_apply`, namely its transpose
> across `ι^* ⊣ ι_*` carries a section of the defining ideal sheaf of `Z` to the universal
> differential `d_{Z'/Y}` of that section followed by the unit of the adjunction.
>
> Since the map of Stacks 060E is an isomorphism, this equation determines the first arrow, so it
> is the whole of that arrow's dependence on `d_{Z'/Y}`.  It holds by construction — it is the
> defining equation of `AlgebraicGeometry.Space.thickeningConormalFirstMap`, recorded so that
> consumers may rewrite with it rather than unfold the definition, as
> `AlgebraicGeometry.Space.conormalModule_eq` and
> `AlgebraicGeometry.Space.conormalSheaf_eq` are for their definitions; what carries the
> mathematical content of the clause is the Stacks 05ZA statement it defers to.

```lean
theorem thickeningConormalFirstMap_comp_thickeningSheafOfDifferentialsMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (he : IsIso (thickeningSheafOfDifferentialsMap B S hS hZ p)) :
    thickeningConormalFirstMap B S hS hZ p he ≫
        thickeningSheafOfDifferentialsMap B S hS hZ p =
      conormalSequenceFirstMap B S hS (thickeningClosedSubspace B S hS hZ) (h' ≫ p)
```

**`AlgebraicGeometry.Space.epi_thickeningConormalSecondMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean#L248). The attribute's comment: “exactness at the right term: the second arrow `h^*Ω_{X/Y} ⟶ Ω_{Z/Y}` is an epimorphism. Granted as `he` that the map of 060E is an isomorphism, and as `hsharp` local surjectivity of `ι♯` (the inverse-image form of the surjectivity clause of 03MB), which is the same hypothesis as in the exactness at the right term of 05ZA”.

> **Stacks 060F, exactness at the right term.**  The second arrow `h^*Ω_{X/Y} ⟶ Ω_{Z/Y}` is an
> epimorphism, so the sequence ends in zero.
>
> It is the isomorphism of Stacks 060E followed by the second arrow of Stacks 05ZA, and the latter
> is an epimorphism by `AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_of_isLocallySurjective`
> under local surjectivity of `ι♯`, which is the hypothesis `hsharp` passed straight through.

```lean
theorem epi_thickeningConormalSecondMap
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (he : IsIso (thickeningSheafOfDifferentialsMap B S hS hZ p))
    (hsharp : Presheaf.IsLocallySurjective
      (SmallEtale.topology B S hS (universalThickeningSubSpace B S hS hZ).obj)
      (structureSharpInverseImage B S hS (universalThickeningInclusion B S hS hZ)).hom) :
    Epi (thickeningConormalSecondMap B S hS hZ p)
```

**`AlgebraicGeometry.Space.thickeningConormalSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallyUnramified.lean#L287). The attribute's comment: “the composite of the two arrows is zero and the short complex is exact at the middle term `h^*Ω_{X/Y}` — the transport across the isomorphism of 060E, which is the whole of the tag's proof. Granted as `he` that the map of 060E is an isomorphism, and as `hzero` and `h05ZA` the same two clauses for the sequence of 05ZA at `Z ⊂ Z'` over the base, which are the two clauses 05ZA leaves open in this tree. Exactness at the right term is separate and is proved: see `epi_thickeningConormalSecondMap`”.

> **Stacks 060F, the two remaining clauses**: the composite of the two arrows is zero, and the
> resulting short complex `𝒞_{Z/X} ⟶ h^*Ω_{X/Y} ⟶ Ω_{Z/Y}` is exact at the middle term.
>
> This is the transport the source's proof performs, and it is all that is proved here: both
> clauses are *granted* for the sequence of Stacks 05ZA at the closed subspace `Z ⊂ Z'` over `Y`,
> as `hzero` and `h05ZA`, and the isomorphism of Stacks 060E carries them across.  The short
> complex of the conclusion is isomorphic to the short complex of Stacks 05ZA, by the identity on
> the two outer terms and that isomorphism on the middle one, so
> `CategoryTheory.ShortComplex.exact_iff_of_iso` transfers exactness.
>
> The two granted clauses are precisely the two clauses that
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentials.lean` leaves open for
> Stacks 05ZA, stated at its first arrow and at its second arrow
> `AlgebraicGeometry.Space.pullbackDifferentialsMap`, so proving them there discharges them here
> verbatim.  Exactness at the right term is not among them: it is proved, by
> `AlgebraicGeometry.Space.epi_thickeningConormalSecondMap`.

```lean
theorem thickeningConormalSequence_exact
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (he : IsIso (thickeningSheafOfDifferentialsMap B S hS hZ p))
    (hzero : conormalSequenceFirstMap B S hS (thickeningClosedSubspace B S hS hZ) (h' ≫ p) ≫
      pullbackDifferentialsMap B S hS (universalThickeningInclusion B S hS hZ) (h' ≫ p) = 0)
    (h05ZA : (ShortComplex.mk _ _ hzero).Exact) :
    ∃ hc : thickeningConormalFirstMap B S hS hZ p he ≫
        thickeningConormalSecondMap B S hS hZ p = 0,
      (ShortComplex.mk _ _ hc).Exact
```

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.exists_conormalSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedConormalSequence.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedConormalSequence.lean#L152).

> Let `h = ι ≫ h' : Z ⟶ X` be formally unramified over `Y`, with universal first order
> neighbourhood `Z ⊂ Z'` over `X` given by `hZ`.  The canonical sequence
> ```
>   𝒞_{Z/X} ⟶ h^*Ω_{X/Y} ⟶ Ω_{Z/Y} ⟶ 0
> ```
> is exact: the composite of its two arrows is zero, it is exact at `h^*Ω_{X/Y}`, and its second
> arrow is an epimorphism.  Its first arrow is induced by `d_{Z'/Y}`: followed by the isomorphism
> `h^*Ω_{X/Y} ≅ ι^*Ω_{Z'/Y}` of Stacks 060E it is the arrow
> `AlgebraicGeometry.Space.conormalSequenceFirstMap` of the closed subspace `Z ⊂ Z'`, whose
> transpose sends a local section of the ideal of `Z` to its differential
> (`AlgebraicGeometry.Space.conormalSequenceIdealDifferential_val_app_apply`).
>
> The sequence of Stacks 05ZA for `Z ⊂ Z'` is exact, and the isomorphism of Stacks 060E carries
> it onto this one.

```lean
theorem exists_conormalSequence_exact (hZ : IsUniversalFirstOrderThickening B S hS Z h')
    (p : X ⟶ Y) :
    ∃ hc : thickeningConormalFirstMap B S hS hZ p
        (hZ.isIso_thickeningSheafOfDifferentialsMap B S hS p) ≫
          thickeningConormalSecondMap B S hS hZ p = 0,
      (ShortComplex.mk _ _ hc).Exact ∧ Epi (thickeningConormalSecondMap B S hS hZ p) ∧
        thickeningConormalFirstMap B S hS hZ p
            (hZ.isIso_thickeningSheafOfDifferentialsMap B S hS p) ≫
          thickeningSheafOfDifferentialsMap B S hS hZ p =
        conormalSequenceFirstMap B S hS (thickeningClosedSubspace B S hS hZ) (h' ≫ p)
```

## Tag 06BE, a lemma

[Tag 06BE](https://stacks.math.columbia.edu/tag/06BE) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_conormalPairSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairExact.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairExact.lean#L242).

> **Stacks 06BE.**  Let `i : Z ⟶ X` and `j : Z ⟶ Y` be formally unramified morphisms of
> algebraic spaces over `S` with `i ≫ g = j`, presented by universal first-order thickenings
> `ti` of `i` and `tj` of `j`.  Then the canonical sequence
>
> ```
>   𝒞_{Z/Y} ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/Y} ⟶ 0
> ```
>
> is exact: the composite of the two arrows is zero, the sequence is exact at `𝒞_{Z/X}`, and the
> second arrow is an epimorphism.  The first arrow is the map of conormal modules of Stacks 060A
> attached to the canonical morphism `Z' ⟶ Z''` of the two thickenings, written as the conormal map
> of Stacks 04CP of its square of closed subspaces; the second is the canonical first arrow of
> Stacks 060F.

```lean
theorem exists_conormalPairSequence_exact (g : X ⟶ Y) {i : Z ⟶ X} {j : Z ⟶ Y}
    (hij : i ≫ g = j) (ti : UniversalFirstOrderThickening B S hS i)
    (tj : UniversalFirstOrderThickening B S hS j) :
    ∃ hc : conormalMap B S hS (thickeningClosedSubspace B S hS ti.isUniversal)
          (thickeningClosedSubspace B S hS tj.isUniversal)
          (universalThickeningComparison B S hS g hij ti tj)
          (ObjectProperty.homMk (universalThickeningSourceMap B S hS ti tj))
          (universalThickeningComparison_square B S hS g hij ti tj) ≫
        thickeningConormalFirstMap B S hS ti.isUniversal g
          (ti.isUniversal.isIso_thickeningSheafOfDifferentialsMap B S hS g) = 0,
      (ShortComplex.mk _ _ hc).Exact ∧
        Epi (thickeningConormalFirstMap B S hS ti.isUniversal g
          (ti.isUniversal.isIso_thickeningSheafOfDifferentialsMap B S hS g))
```

## Tag 06BF, a lemma

[Tag 06BF](https://stacks.math.columbia.edu/tag/06BF) in the Stacks Project.

**`AlgebraicGeometry.Space.universalThickeningCompConormalSequence_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalSequenceCompositionExact.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalSequenceCompositionExact.lean#L223). The attribute's comment: “clause (2): the composite of the two maps of the sequence vanishes”.

> **The composite of the two arrows of the conormal sequence of the composition vanishes.**
> By the composition law of part (3) of Stacks 04G2,
> `AlgebraicGeometry.Space.conormalMap_comp`, the composite is the map of Stacks 04CP attached to
> the outer rectangle, read through the composition comparison of Stacks 03LU, which is an
> isomorphism.  The lower edge of that rectangle is the inclusion of the fibre product
> `Y ×_{Y'} Z'` into `Z'` followed by the morphism `h : Z' ⟶ Y'` of clause (1) of Stacks 06BF, and
> that composite factors through the closed subspace `Y ⊆ Y'` by the structure morphism
> `AlgebraicGeometry.Space.universalThickeningCompStructure` of the fibre product — which is what
> makes the fibre product a fibre product.  So the map of the outer rectangle vanishes by
> `AlgebraicGeometry.Space.conormalMap_eq_zero_of_factorization`.

```lean
public theorem universalThickeningCompConormalSequence_comp_eq_zero :
    modulePullbackMap B S hS
          (preimageProjection B S hS
            (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
            ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩)
          (universalThickeningCompConormalLowerMap B S hS i hZ hY hfac) ≫
      universalThickeningCompConormalRightMap B S hS i hZ hY hfac = 0
```

**`AlgebraicGeometry.Space.exact_universalThickeningCompConormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalSequenceCompositionExact.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalSequenceCompositionExact.lean#L320). The attribute's comment: “clause (2): exactness at the middle term”.

> **Exactness at `𝒞_{Z/X}` of the conormal sequence of the composition** — the middle clause of
> Stacks 06BD in this presentation.  `AlgebraicGeometry.Space.exact_conormalShortComplex_preimage`
> is that clause for a closed subspace inside the inverse image of a closed subspace downstairs,
> which is what the fibre product `Y ×_{Y'} Z'` presents; its four comparison arguments are
> discharged by the structural equations above, each of them an equation of single arrows.
>
> With `AlgebraicGeometry.Space.universalThickeningCompConormalSequence_comp_eq_zero` above, which
> supplies the vanishing the short complex is formed from, this is the middle-exactness assertion
> of clause (2) of Stacks 06BF; the companion clauses of that tag are registered in
> `StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean`.

```lean
public theorem exact_universalThickeningCompConormalSequence :
    (ShortComplex.mk _ _
      (universalThickeningCompConormalSequence_comp_eq_zero B S hS i hZ hY hfac)).Exact
```

**`AlgebraicGeometry.Space.universalThickeningCompMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean#L198). The attribute's comment: “clause (1): the morphism Z' ⟶ Y'”.

> **Stacks 06BF, clause (1), the morphism `Z' ⟶ Y'`.**  Let `Z ⊂ Z'` be a universal
> first-order thickening of `Z` over `X` and let `Y ⊂ Y'` be a universal first-order thickening of
> `Y` over `X`, and let the structure morphism of `Z` factor through `Y`.  The morphism
> `h : Z' ⟶ Y'` is the canonical morphism of Stacks 060A for the square with `g = 𝟙 X`, that is
> the unique morphism restricting to `i : Z ⟶ Y` and lying over `X`.

```lean
noncomputable def universalThickeningCompMap : Z' ⟶ Y'
```

**`AlgebraicGeometry.Space.isUniversalFirstOrderThickening_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean#L272). The attribute's comment: “clause (1): Y ×\_\{Y'} Z' is the universal first-order thickening of Z over Y, the square-zero condition inside the fibre product being hypothesised”.

> **Stacks 06BF, clause (1), the universal first-order thickening of `Z` over `Y`.**  With the
> morphism `h : Z' ⟶ Y'` of `AlgebraicGeometry.Space.universalThickeningCompMap`, the fibre
> product `Y ×_{Y'} Z'` is a universal first-order thickening of `Z` over `Y`, with structure
> morphism the projection to `Y`.
>
> A morphism `T' ⟶ Y ×_{Y'} Z'` is a pair of morphisms to `Y` and to `Z'` agreeing over `Y'`.
> Given a solid diagram over `Y` built from a first-order thickening `T ⊂ T'` and a morphism
> `T ⟶ Z`, the morphism to `Y` is the one the diagram supplies and the morphism `e : T' ⟶ Z'` is
> the unique one furnished by the universal property of `Z ⊂ Z'` over `X`.  That the two agree
> over `Y'` is uniqueness in the universal property of `Y ⊂ Y'`: both composites restrict to
> `Z ⟶ Y` on `T` and lie over `X`, the first because `h` restricts to `i` and lies over `X`.
> Uniqueness of the resulting morphism is uniqueness of `e` together with the fact that the
> inclusion of the fibre product into `Z'` is a monomorphism.
>
> That the copy of `Z` is a first-order thickening of `Y ×_{Y'} Z'` is a hypothesis; see the
> implementation notes of this file.

```lean
theorem isUniversalFirstOrderThickening_comp
    (hfirst : IsFirstOrderThickening B S hS
      (universalThickeningCompFibre B S hS i hZ hY hfac)
      (universalThickeningCompSub B S hS i hZ hY hfac)) :
    IsUniversalFirstOrderThickening B S hS
      (universalThickeningCompSub B S hS i hZ hY hfac)
      (universalThickeningCompStructure B S hS i hZ hY hfac)
```

**`AlgebraicGeometry.Space.epi_conormalMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningComposition.lean#L306). The attribute's comment: “clause (2): exactness at the right term, the canonical map 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y} being surjective”.

> **Stacks 06BF, clause (2), at the right term.**  The canonical map
> `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of Stacks 04CP — the right-hand map of the conormal sequence of the
> composition — is surjective.
>
> By Stacks 0607 the conormal module of a formally unramified morphism is the conormal module of
> its source inside its universal first-order thickening, so `𝒞_{Z/X}` is the conormal module of
> `Z` in `Z'` and, by clause (1), `𝒞_{Z/Y}` is the conormal module of the copy of `Z` inside
> `Y ×_{Y'} Z'`.  The map between them is the one of Stacks 04CP for the inclusion
> `Y ×_{Y'} Z' ⟶ Z'`, and surjectivity is the surjectivity clause of Stacks 04CQ,
> `AlgebraicGeometry.Space.epi_conormalMap`, for that inverse-image configuration.
>
> The left-hand map of the sequence is `AlgebraicGeometry.Space.universalThickeningConormalMap`
> for the square of `AlgebraicGeometry.Space.universalThickeningComp_square`; exactness in the
> middle is not proved, see the "What is not proved" section of this file.

```lean
theorem epi_conormalMap_comp :
    Epi (conormalMap B S hS
      (preimageSubspace B S hS
        (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩)
      ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩
      (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
      (preimageProjection B S hS
        (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩)
      (conormalEtaleRestrictionSquare B S hS
        (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩))
```

**`AlgebraicGeometry.Space.isUniversalFirstOrderThickening_comp'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningCompositionComplex.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningCompositionComplex.lean#L155). The attribute's comment: “clause (1): Y ×\_\{Y'} Z' is the universal first-order thickening of Z over Y”.

> **Stacks 06BF, clause (1), the universal first-order thickening of `Z` over `Y`.**  With the
> morphism `h : Z' ⟶ Y'` of `AlgebraicGeometry.Space.universalThickeningCompMap`, the fibre
> product `Y ×_{Y'} Z'` is a universal first-order thickening of `Z` over `Y`, with structure
> morphism the projection to `Y`.
>
> A morphism `T' ⟶ Y ×_{Y'} Z'` is a pair of morphisms to `Y` and to `Z'` agreeing over `Y'`.
> Given a solid diagram over `Y` built from a first-order thickening `T ⊂ T'` and a morphism
> `T ⟶ Z`, the morphism to `Y` is the one the diagram supplies and the morphism `e : T' ⟶ Z'` is
> the unique one furnished by the universal property of `Z ⊂ Z'` over `X`.  That the two agree
> over `Y'` is uniqueness in the universal property of `Y ⊂ Y'`: both composites restrict to
> `Z ⟶ Y` on `T` and lie over `X`, the first because `h` restricts to `i` and lies over `X`.
> Uniqueness of the resulting morphism is uniqueness of `e` together with the fact that the
> inclusion of the fibre product into `Z'` is a monomorphism.
>
> That the copy of `Z` is a first-order thickening of `Y ×_{Y'} Z'` needs nothing of the fibre
> product: it is the inverse image of `Z ⊂ Z'` along the inclusion `Y ×_{Y'} Z' ⟶ Z'`, so it is
> one by the inverse-image clause of Stacks 09ZX,
> `AlgebraicGeometry.Space.isFirstOrderThickening_preimage`.

```lean
theorem isUniversalFirstOrderThickening_comp' :
    IsUniversalFirstOrderThickening B S hS
      (universalThickeningCompSub B S hS i hZ hY hfac)
      (universalThickeningCompStructure B S hS i hZ hY hfac)
```

**`AlgebraicGeometry.Space.universalThickeningConormalMap_comp_conormalMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningCompositionComplex.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningCompositionComplex.lean#L236). The attribute's comment: “clause (2): the sequence is a complex, the composite of i^*𝒞\_\{Y/X} ⟶ 𝒞\_\{Z/X} and 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y} being zero”.

> **Stacks 06BF, clause (2): the sequence is a complex.**  The composite of the two maps
> `i^*𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of the conormal sequence of the composition is zero.
>
> The left-hand map is the inverse image, along the projection of the copy of `Z` inside
> `Y ×_{Y'} Z'`, of the canonical map of Stacks 060A at the square of
> `AlgebraicGeometry.Space.universalThickeningComp_square`, and the right-hand map is the map of
> Stacks 04CP for the inclusion `Y ×_{Y'} Z' ⟶ Z'`.  So the composite is the conormal map of the
> outer rectangle of those two stacked squares, by part (3) of Stacks 04G2, and the ambient
> morphism of that rectangle is `Y ×_{Y'} Z' ⟶ Z' ⟶ Y'`, which factors through the inclusion of
> `Y` by `AlgebraicGeometry.Space.universalThickeningCompFibreInclusion_comp_map`.  A conormal map
> whose ambient morphism factors through the lower closed subspace is zero, the defining ideal of
> that subspace being the kernel of the comorphism of its inclusion; that is
> `AlgebraicGeometry.Space.comp_conormalMap_eq_zero_of_factors`.
>
> The left-hand map is written here as that map of Stacks 04CP rather than as
> `AlgebraicGeometry.Space.universalThickeningConormalMap`; the two are the same morphism, by
> `AlgebraicGeometry.Space.universalThickeningCompConormalMap_eq`.  Writing it the second way makes
> the statement one the kernel cannot check: the definitional comparison would then sit inside the
> inverse image of modules and inside a composition, which is exactly what the implementation notes
> of `StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleBaseChangeEpi.lean` record as beyond the
> budget.
>
> A consumer wanting the arrows of this sequence should take them from *this* theorem, as
> `CategoryTheory.ShortComplex.f` and `CategoryTheory.ShortComplex.g` of
> `CategoryTheory.ShortComplex.mk _ _` applied to it, which is what
> `AlgebraicGeometry.Space.universalThickeningCompConormalSequence_shortExact'`, Stacks 06CC, does.
> Crossing the two spellings by rewriting with
> `AlgebraicGeometry.Space.universalThickeningCompConormalMap_eq` is *not* an available route once
> the arrow sits under the inverse image of modules, and neither is naming either arrow in a
> definition of its own — the section *How the sequence is written* of the file of that theorem
> records what each of those costs.

```lean
theorem universalThickeningConormalMap_comp_conormalMap_eq_zero :
    (modulePullback B S hS
          (preimageProjection B S hS
            (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
            ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩)).map
        (conormalMap B S hS ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩
          ⟨Y, (IsNthOrderThickening.isThickening B S hS hY.firstOrder).1⟩
          (universalThickeningCompMap B S hS i hZ hY hfac)
          (ObjectProperty.homMk i)
          (universalThickeningComp_subspace_square B S hS i hZ hY hfac)) ≫
      conormalMap B S hS
        (preimageSubspace B S hS
          (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
          ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩)
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩
        (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
        (preimageProjection B S hS
          (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
          ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩)
        (conormalEtaleRestrictionSquare B S hS
          (universalThickeningCompFibreInclusion B S hS i hZ hY hfac)
          ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩) = 0
```

**`AlgebraicGeometry.Space.exact_and_epi_universalThickeningCompConormalMapSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningCompositionExact.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalThickeningCompositionExact.lean#L89). The attribute's comment: “clause (2): the conormal sequence i^*𝒞\_\{Y/X} ⟶ 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y} ⟶ 0 is exact”.

> **Stacks 06BF, clause (2).**  Let `Z ⟶ Y ⟶ X` be morphisms of algebraic spaces, `Z ⊂ Z'`
> and `Y ⊂ Y'` universal first-order thickenings over `X`, and `h : Z' ⟶ Y'` the morphism of
> clause (1).  The conormal sequence
>
> `i^*𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0`
>
> is exact: exact at `𝒞_{Z/X}`, and its right-hand map is an epimorphism.  Here `𝒞_{Z/X}` is the
> conormal module of `Z ⊂ Z'`, `𝒞_{Y/X}` that of `Y ⊂ Y'`, and `𝒞_{Z/Y}` that of the copy of `Z`
> inside the universal first-order thickening `Y ×_{Y'} Z' = h⁻¹(Y)` of clause (1); the two maps
> are those of Stacks 04CP, for the square of `Z ⊆ Z'` over `Y ⊆ Y'` with ambient morphism `h`
> (pulled back to the copy of `Z`) and for the inclusion `h⁻¹(Y) ⟶ Z'`.  They are the arrows of
> `AlgebraicGeometry.Space.universalThickeningConormalMap_comp_conormalMap_eq_zero`, by
> `AlgebraicGeometry.Space.universalThickeningCompConormalSequence_f_eq` and `..._g_eq`.
>
> Exactness in the middle is `AlgebraicGeometry.Space.exact_conormalMap_square` at that square;
> the epimorphism is the surjectivity clause of Stacks 04CQ for the inclusion `h⁻¹(Y) ⟶ Z'`.

```lean
theorem exact_and_epi_universalThickeningCompConormalMapSquare :
    (ShortComplex.mk _ _ (conormalMap_square_comp_eq_zero B S hS
        (universalThickeningCompMap B S hS i hZ hY hfac)
        ⟨Y, (IsNthOrderThickening.isThickening B S hS hY.firstOrder).1⟩
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩
        (ObjectProperty.homMk i)
        (universalThickeningComp_subspace_square B S hS i hZ hY hfac))).Exact ∧
      Epi (ShortComplex.mk _ _ (conormalMap_square_comp_eq_zero B S hS
        (universalThickeningCompMap B S hS i hZ hY hfac)
        ⟨Y, (IsNthOrderThickening.isThickening B S hS hY.firstOrder).1⟩
        ⟨Z, (IsNthOrderThickening.isThickening B S hS hZ.firstOrder).1⟩
        (ObjectProperty.homMk i)
        (universalThickeningComp_subspace_square B S hS i hZ hY hfac))).g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.15, Tag 0601](https://stacks.math.columbia.edu/tag/0601)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
