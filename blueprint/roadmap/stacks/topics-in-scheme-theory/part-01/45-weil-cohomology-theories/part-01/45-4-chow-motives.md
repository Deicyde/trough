---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.ChowMotiveCat, Stacks.WeilCohomology.ChowMotiveCat.homEquiv, Stacks.WeilCohomology.ChowMotiveCat.homEquiv_id, Stacks.WeilCohomology.ChowMotiveCat.homEquiv_comp, Stacks.WeilCohomology.ChowMotiveCat.linear, Stacks.WeilCohomology.ChowMotiveCat.h, Stacks.WeilCohomology.ChowMotiveCat.h_obj_projector, Stacks.WeilCohomology.ChowMotiveCat.h_obj_twist
statement: formalized
proof: formalized
---

# 45.4 Chow motives

Section 45.4 of the Stacks Project, [Tag 0FG9](https://stacks.math.columbia.edu/tag/0FG9). 10 tags here are carried by 49 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FGA, a lemma

[Tag 0FGA](https://stacks.math.columbia.edu/tag/0FGA) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L80). The attribute's comment: “the category M\_k of Chow motives (X, p, m) over k”.

> The category `M_k` of Chow motives over `k`. An object is a triple `(X, p, m)` of a smooth
> projective scheme `X` over `k`, a projector `p ∈ Corr⁰(X, X)` (`p ∘ p = p`) and a twist `m ∈ ℤ`;
> a morphism `(X, p, m) ⟶ (Y, q, n)` is a correspondence in `q ∘ Corr^{n-m}(X, Y) ∘ p`, and
> composition is composition of correspondences.

```lean
abbrev ChowMotiveCat : Type (u + 1)
```

**`Stacks.WeilCohomology.ChowMotiveCat.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L269). The attribute's comment: “Hom((X, p, m), (Y, q, n)) = q o Corr^\{n-m}(X, Y) o p, as Q-vector spaces”.

> The morphisms of `M_k` from `(X, p, m)` to `(Y, q, n)` are the correspondences in
> `q ∘ Corr^{n-m}(X, Y) ∘ p ⊂ Corr^{n-m}(X, Y)`: an isomorphism of `ℚ`-vector spaces sending a
> morphism to the underlying correspondence.

```lean
def homEquiv (M N : ChowMotiveCat k) : (M ⟶ N) ≃ₗ[ℚ] corrHom M N
```

**`Stacks.WeilCohomology.ChowMotiveCat.homEquiv_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L296). The attribute's comment: “the identity of (X, p, m) is p”.

> The identity morphism of the motive `(X, p, m)` is the projector `p` (compared after
> `DirectSum.of`, the degree `m - m` being `0`).

```lean
theorem homEquiv_id (M : ChowMotiveCat k) :
    DirectSum.of (fun i ↦ SmoothProjectiveCorr M.scheme M.scheme i) (M.twist - M.twist)
        (homEquiv M M (𝟙 M)).1 =
      DirectSum.of (fun i ↦ SmoothProjectiveCorr M.scheme M.scheme i) 0 M.projector
```

**`Stacks.WeilCohomology.ChowMotiveCat.homEquiv_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L309). The attribute's comment: “composition of morphisms of motives is composition of correspondences”.

> Composition of morphisms of motives is composition of correspondences: for
> `f : (X, p, m) ⟶ (Y, q, n)` and `g : (Y, q, n) ⟶ (Z, r, l)` the correspondence of `f ≫ g` is
> `g ∘ f` (compared after `DirectSum.of`, the degrees `l - m` and `(n - m) + (l - n)` being
> equal).

```lean
theorem homEquiv_comp {M N P : ChowMotiveCat k} (f : M ⟶ N) (g : N ⟶ P) :
    DirectSum.of (fun i ↦ SmoothProjectiveCorr M.scheme P.scheme i) (P.twist - M.twist)
        (homEquiv M P (f ≫ g)).1 =
      DirectSum.of (fun i ↦ SmoothProjectiveCorr M.scheme P.scheme i)
        ((N.twist - M.twist) + (P.twist - N.twist))
        ((canonicalCorrespondenceCompositionData k).comp (homEquiv M N f).1
          (homEquiv N P g).1)
```

**`Stacks.WeilCohomology.ChowMotiveCat.linear`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L324). The attribute's comment: “M\_k is a Q-linear category”.

> The category `M_k` of Chow motives is `ℚ`-linear: the morphism spaces are the `ℚ`-vector
> spaces `q ∘ Corr^{n-m}(X, Y) ∘ p` and composition is `ℚ`-bilinear, composition of
> correspondences being so (Stacks 0FG0 (1)).

```lean
abbrev linear : Linear ℚ (ChowMotiveCat k)
```

**`Stacks.WeilCohomology.ChowMotiveCat.h`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L335). The attribute's comment: “the contravariant functor h, h(X) = (X, 1, 0), h(f) = [Gamma\_f]”.

> The contravariant functor `h : {smooth projective schemes over k} ⟶ M_k`,
> `h(X) = (X, 1, 0)` with `1 = [Δ_X]` the identity correspondence, and
> `h(f) = [Γ_f] ∈ Corr⁰(X, Y)` for `f : Y ⟶ X`.

```lean
def h : ((SmoothProjectiveScheme k).FullSubcategory)ᵒᵖ ⥤ ChowMotiveCat k
```

**`Stacks.WeilCohomology.ChowMotiveCat.h_obj_projector`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L354). The attribute's comment: “h(X) = (X, 1, 0): the projector”.

> The projector of `h(X)` is `1 = [Δ_X] ∈ Corr⁰(X, X)`.

```lean
theorem h_obj_projector (X : (SmoothProjectiveScheme k).FullSubcategory) :
    ((h k).obj (Opposite.op X)).projector = correspondenceDiagonal k X
```

**`Stacks.WeilCohomology.ChowMotiveCat.h_obj_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L360). The attribute's comment: “h(X) = (X, 1, 0): the twist”.

> The twist of `h(X)` is `0`.

```lean
theorem h_obj_twist (X : (SmoothProjectiveScheme k).FullSubcategory) :
    ((h k).obj (Opposite.op X)).twist = 0
```

**`Stacks.WeilCohomology.ChowMotiveCat.homEquiv_h_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Motives.lean#L367). The attribute's comment: “h(f) = [Gamma\_f]”.

> For `f : Y ⟶ X`, the correspondence of `h(f) : h(X) ⟶ h(Y)` is the graph class
> `[Γ_f] ∈ Corr⁰(X, Y)`.

```lean
theorem homEquiv_h_map {X Y : (SmoothProjectiveScheme k).FullSubcategory} (f : Y ⟶ X) :
    (homEquiv _ _ ((h k).map f.op)).1 = graphCorrespondenceSP f
```

**`Stacks.WeilCohomology.CorrespondenceStructure.Motive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean#L142). The attribute's comment: “the category M\_k of Chow motives over k, whose objects are the triples (X,p,m)”.

> **Stacks Project, Tag 0FGA.** The category `M_k` of Chow motives over `k`: the Karoubi
> envelope of the category of correspondences. An object is a pair of an object of the ambient
> category — a smooth projective scheme together with its Tate twist — and a projector in
> `Corr⁰(X, X)`, that is a triple `(X, p, m)`; a morphism `(X, p, m) ⟶ (Y, q, n)` is a
> correspondence in `Corr^{n-m}(X, Y)` fixed by the two projectors.

```lean
abbrev Motive (S : CorrespondenceStructure.{v, u, w} D)
```

**`Stacks.WeilCohomology.CorrespondenceStructure.hom_motive_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean#L148). The attribute's comment: “Hom((X,p,m),(Y,q,n)) = q o Corr^\{n-m}(X,Y) o p”.

> **Stacks Project, Tag 0FGA.** The morphisms of `M_k` are the correspondences cut out by the
> two projectors: `Hom((X, p, m), (Y, q, n)) = q ∘ Corr^{n-m}(X, Y) ∘ p`.

```lean
theorem hom_motive_iff (S : CorrespondenceStructure.{v, u, w} D) {M N : S.Motive}
    (c : M.X ⟶ N.X) :
    (∃ f : M ⟶ N, f.f = c) ↔ ∃ c₀ : M.X ⟶ N.X, c = M.p ≫ c₀ ≫ N.p
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motiveFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean#L174). The attribute's comment: “the functor h into M\_k, with h(X) = (X,1,0) and h(f) = [Gamma\_f]”.

> **Stacks Project, Tag 0FGA.** The functor `h` of Stacks 0FGA, from the ambient category of
> smooth projective schemes over `k` to the category of Chow motives: `h(X) = (X, 1, 0)` is the
> motive of `X` with the identity as projector and no twist, and `h(f) = [Γ_f]` is the graph of a
> morphism.
>
> The source's `h` is contravariant on schemes, `h(f) = [Γ_f] ∈ Corr⁰(X, Y)` for `f : Y → X`,
> while `Stacks.WeilCohomology.CorrespondenceStructure.graph` is covariant on the ambient
> category; so the ambient category here is the opposite of the category of smooth projective
> schemes over `k` enlarged by the Tate twists, and `h` is then the source's functor.

```lean
def motiveFunctor (S : CorrespondenceStructure.{v, u, w} D) : D ⥤ S.Motive
```

**`Stacks.WeilCohomology.CorrespondenceStructure.linear`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Category.lean#L201). The attribute's comment: “M\_k is a Q-linear category, given the Q-linear structure on correspondences”.

> **Stacks Project, Tag 0FGA.** The category `M_k` of Chow motives is `ℚ`-linear, the
> category of correspondences being so. The `ℚ`-linear structure of the correspondence spaces is
> the content of Stacks 0FG2 and enters as a hypothesis; what is proved is that it passes to the
> Karoubi envelope.

```lean
def linear (S : CorrespondenceStructure.{v, u, w} D) [Preadditive S.Obj] [Linear ℚ S.Obj] :
    Linear ℚ S.Motive
```

**`Stacks.WeilCohomology.MotiveCalculus.mem_homSubmodule_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean#L403). The attribute's comment: “the morphisms of the category of motives are the sandwiched correspondences”.

> A total correspondence is a morphism of motives `(X, p, m) → (Y, q, n)` exactly when it is a
> sandwich `p ∘ a ∘ q` of a correspondence `a` homogeneous of degree `n - m`: the fixed set of the
> idempotent sandwich operator is its image.

```lean
theorem mem_homSubmodule_iff {M N : ChowMotive C D.toCorrespondenceCalculus}
    {f : TotalCorr C (motiveObj M) (motiveObj N)} :
    f ∈ D.homSubmodule M N ↔
      ∃ a ∈ corrGrade C (motiveObj M) (motiveObj N) (N.twist - M.twist),
        D.compTotal (motiveObj M) (motiveObj N) (motiveObj N)
          (D.compTotal (motiveObj M) (motiveObj M) (motiveObj N) (D.projectorTotal M) a)
          (D.projectorTotal N) = f
```

**`Stacks.WeilCohomology.MotiveCalculus.category`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Representability.lean#L428). The attribute's comment: “the category of Chow motives”.

> The category of Chow motives: Chow motives as objects, the sandwiched correspondences of
> degree `n - m` as morphisms, the projector as the identity and composition of correspondences as
> composition.

```lean
instance category : Category.{u} D.Obj
```

## Tag 0FGB, a lemma

[Tag 0FGB](https://stacks.math.columbia.edu/tag/0FGB) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.hasKernel_of_idem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Karoubian.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Karoubian.lean#L44).

> **Stacks Project, Tag 0FGB.** The category `M_k` of Chow motives is Karoubian in the sense of
> Homology, Definition 09SG: every idempotent endomorphism `a` of a motive `M` has a kernel.

```lean
theorem hasKernel_of_idem (M : ChowMotiveCat k) (a : M ⟶ M) (ha : a ≫ a = a) : HasKernel a
```

## Tag 0FGC, a lemma

[Tag 0FGC](https://stacks.math.columbia.edu/tag/0FGC) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.monoidalCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L74). The attribute's comment: “M\_k is monoidal for (X,p,m) ⊗ (Y,q,n) = (X × Y, p ⊗ q, m + n), unit (Spec k, 1, 0)”.

> **Stacks Project, Tag 0FGC.** The category `M_k` of Chow motives is monoidal for
> `(X, p, m) ⊗ (Y, q, n) = (X × Y, p ⊗ q, m + n)`, with the tensor product of correspondences on
> morphisms, unit `𝟏 = (Spec(k), 1, 0)`, and the associativity constraint of correspondences (the
> graph of the associativity isomorphism of products of schemes) cut down by the projectors.

```lean
instance monoidalCategory : MonoidalCategory (ChowMotiveCat k)
```

**`Stacks.WeilCohomology.ChowMotiveCat.braidedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L81). The attribute's comment: “the commutativity constraint of M\_k”.

> **Stacks Project, Tag 0FGC.** The category `M_k` of Chow motives is braided by the
> commutativity constraint of correspondences, the graph of the factor switch
> `X × Y ≅ Y × X`, cut down by the projectors.

```lean
instance braidedCategory : BraidedCategory (ChowMotiveCat k)
```

**`Stacks.WeilCohomology.ChowMotiveCat.symmetricCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L87). The attribute's comment: “M\_k is symmetric monoidal”.

> **Stacks Project, Tag 0FGC.** The category `M_k` of Chow motives is symmetric monoidal with
> the obvious associativity and commutativity constraints and with unit `𝟏 = (Spec(k), 1, 0)`.

```lean
instance symmetricCategory : SymmetricCategory (ChowMotiveCat k)
```

**`Stacks.WeilCohomology.ChowMotiveCat.tensorObj_mk'_p`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L131). The attribute's comment: “(X, p, m) ⊗ (Y, q, n) = (X × Y, p ⊗ q, m + n)”.

> **Stacks Project, Tag 0FGC.** The tensor product of motives on objects:
> `(X, p, m) ⊗ (Y, q, n) = (X × Y, p ⊗ q, m + n)`; this is the projector, `p ⊗ q`, the tensor product
> of correspondences (`tensorObj_mk'_scheme` and `tensorObj_mk'_twist` give `X × Y` and `m + n`).

```lean
theorem tensorObj_mk'_p (X Y : (SmoothProjectiveScheme k).FullSubcategory)
    (p : SmoothProjectiveCorr X X 0)
    (q : SmoothProjectiveCorr Y Y 0)
    (hp : (canonicalCorrespondenceCompositionData k).comp p p = p)
    (hq : (canonicalCorrespondenceCompositionData k).comp q q = q) (m n : ℤ) :
    (mk' X p hp m ⊗ mk' Y q hq n).p = homOf (0 + 0) (CorrespondenceCategory.tensorCorr 0 0 p q)
```

**`Stacks.WeilCohomology.ChowMotiveCat.tensorHom_val_eq_homOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L161). The attribute's comment: “on morphisms, (a, a') ↦ a ⊗ a' with ⊗ the tensor product of correspondences”.

> **Stacks Project, Tag 0FGC.** The tensor product of morphisms of motives is the tensor
> product of correspondences: if `f : (X, p, m) ⟶ (Y, q, n)` is the correspondence
> `a ∈ Corr^{n-m}(X, Y)` and `f' : (X', p', m') ⟶ (Y', q', n')` is `a' ∈ Corr^{n'-m'}(X', Y')`, then
> `f ⊗ f'` is `a ⊗ a' ∈ Corr^{(n-m)+(n'-m')}(X × X', Y × Y')`.

```lean
theorem tensorHom_val_eq_homOf {M N M' N' : ChowMotiveCat k} (f : M ⟶ N) (f' : M' ⟶ N')
    {r r' : ℤ} (a : SmoothProjectiveCorr M.scheme N.scheme r)
    (a' : SmoothProjectiveCorr M'.scheme N'.scheme r') (ha : f.val = homOf r a)
    (ha' : f'.val = homOf r' a') :
    (f ⊗ₘ f').val = homOf (r + r') (CorrespondenceCategory.tensorCorr r r' a a')
```

**`Stacks.WeilCohomology.ChowMotiveCat.tensorUnit_eq_tate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L171). The attribute's comment: “the unit of M\_k is 1 = (Spec k, 1, 0)”.

> **Stacks Project, Tag 0FGC.** The unit of `M_k` is `𝟏 = 𝟏(0) = (Spec(k), 1, 0)`.

```lean
theorem tensorUnit_eq_tate : 𝟙_ (ChowMotiveCat k) = tate k 0
```

**`Stacks.WeilCohomology.ChowMotiveCat.associator_hom_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L178). The attribute's comment: “the associativity constraint of M\_k is the obvious one”.

> **Stacks Project, Tag 0FGC.** The associativity constraint of `M_k` is the obvious one: the
> graph of the associativity isomorphism `(X × Y) × Z ≅ X × (Y × Z)`, cut down by the
> projectors.

```lean
theorem associator_hom_val (M N P : ChowMotiveCat k) :
    (α_ M N P).hom.val =
      ((M ⊗ N) ⊗ P).p ≫ graphHom (α_ M.scheme N.scheme P.scheme).inv
```

**`Stacks.WeilCohomology.ChowMotiveCat.braiding_hom_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesMonoidal.lean#L186). The attribute's comment: “the commutativity constraint of M\_k is the obvious one”.

> **Stacks Project, Tag 0FGC.** The commutativity constraint of `M_k` is the obvious one: the
> graph of the factor switch `X × Y ≅ Y × X`, cut down by the projectors.

```lean
theorem braiding_hom_val (M N : ChowMotiveCat k) :
    (β_ M N).hom.val = (M ⊗ N).p ≫ graphHom (β_ M.scheme N.scheme).inv
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motiveMonoidalCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean#L58). The attribute's comment: “M\_k is monoidal for (X,p,m) ⊗ (Y,q,n) = (X × Y, p ⊗ q, m+n)”.

> The category `M_k` of Chow motives is monoidal for the tensor product
> `(X, p, m) ⊗ (Y, q, n) = (X × Y, p ⊗ q, m + n)`, given the monoidal structure on the category of
> correspondences, which is taken as a hypothesis and passes to the Karoubi envelope.

```lean
def motiveMonoidalCategory : MonoidalCategory S.Motive
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motiveSymmetricCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean#L65). The attribute's comment: “M\_k is symmetric monoidal with unit 1 = (Spec(k), 1, 0)”.

> The category `M_k` of Chow motives is symmetric monoidal, with the associativity and
> commutativity constraints of the category of correspondences cut down by the projectors, and with
> unit `𝟏 = (Spec(k), 1, 0)`.

```lean
def motiveSymmetricCategory : SymmetricCategory S.Motive
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motive_associator_hom_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean#L83). The attribute's comment: “the associativity constraint of M\_k is the obvious one”.

> The associativity constraint of `M_k` is the graph of the associativity constraint of the
> ambient category, cut down by the projectors.

```lean
theorem motive_associator_hom_f (M N P : S.Motive) :
    (α_ M N P).hom.f = ((M ⊗ N) ⊗ P).p ≫ S.graph (α_ M.X.as N.X.as P.X.as).hom
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motive_braiding_hom_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean#L90). The attribute's comment: “the commutativity constraint of M\_k is the obvious one”.

> The commutativity constraint of `M_k` is the graph of the factor switch of the ambient
> category, cut down by the projectors.

```lean
theorem motive_braiding_hom_f (M N : S.Motive) :
    (β_ M N).hom.f = (M ⊗ N).p ≫ S.graph (β_ M.X.as N.X.as).hom
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motive_tensorUnit_as`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean#L97). The attribute's comment: “the unit of M\_k is 1 = (Spec(k), 1, 0)”.

> The scheme underlying the unit motive `𝟏 = (Spec(k), 1, 0)` is `Spec(k)`, the unit of the
> ambient category.

```lean
theorem motive_tensorUnit_as : (𝟙_ S.Motive).X.as = 𝟙_ D
```

**`Stacks.WeilCohomology.CorrespondenceStructure.motive_tensorUnit_p`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/MonoidalStructure.lean#L102). The attribute's comment: “the projector of the unit of M\_k is the diagonal 1”.

> The projector of the unit motive `𝟏 = (Spec(k), 1, 0)` is the diagonal correspondence.

```lean
theorem motive_tensorUnit_p : (𝟙_ S.Motive).p = S.id (𝟙_ D)
```

## Tag 0FGD, a lemma

[Tag 0FGD](https://stacks.math.columbia.edu/tag/0FGD) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.projectiveLinePointFibreMotiveIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineSummands.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineSummands.lean#L112). The attribute's comment: “part (1): the motive (P¹\_k, c₀, 0) is isomorphic to 1 = (Spec k, 1, 0), in the category of Chow motives built on the actual composition of correspondences”.

> **Stacks Project, Tag 0FGD (1).** For a rational point `x` of `X = P¹_k`, the motive
> `(X, c₀, 0)`, with `c₀ = [x × X]`, is isomorphic to `1 = (Spec k, 1, 0)`. The mutually inverse
> morphisms are the graph classes of the structure morphism `X → Spec k` and of the point
> `x : Spec k → X`.

```lean
def projectiveLinePointFibreMotiveIso :
    mk' (projectiveLineObj k) (projectiveLinePointFibreCorr x hx)
      (projectiveLinePointFibreCorr_comp_self x hx) 0 ≅ tate k 0
```

**`Stacks.WeilCohomology.ChowMotiveCat.projectiveLineFibrePointMotiveIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineSummands.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineSummands.lean#L126). The attribute's comment: “part (2): the motive (P¹\_k, c₂, 0) is isomorphic to 1(-1) = (Spec k, 1, -1), with b' ∘ a' = 1 and a' ∘ b' = c₂ proved by intersecting the actual cycles”.

> **Stacks Project, Tag 0FGD (2).** For a rational point `x` of `X = P¹_k`, the motive
> `(X, c₂, 0)`, with `c₂ = [X × x]`, is isomorphic to `1(-1) = (Spec k, 1, -1)`. The mutually
> inverse morphisms are the class `a' ∈ Corr¹(Spec k, X)` of the point `x` and the fundamental class
> `b' ∈ Corr^{-1}(X, Spec k)`, whose compositions `b' ∘ a' = 1` and `a' ∘ b' = c₂` are computed by
> intersecting cycles.

```lean
def projectiveLineFibrePointMotiveIso : lefschetzMotive x hx ≅ tate k (-1)
```

**`Stacks.WeilCohomology.CorrespondenceStructure.constantGraphMotiveIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ProjectiveLineSummands.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/ProjectiveLineSummands.lean#L224). The attribute's comment: “part (1): the motive (X, c\_0, 0) is isomorphic to 1 = (Spec k, 1, 0)”.

> **Stacks Project, Tag 0FGD (1).** The motive `(X, c₀, 0)` is isomorphic to the motive
> `h(Spec k) = 1 = (Spec k, 1, 0)`.
>
> The graph classes of the structure morphism and of the rational point are the source's
> `a ∈ Corr⁰(Spec k, X)` and `b ∈ Corr⁰(X, Spec k)`. Functoriality of the graph turns the identity
> `x ≫ (X → Spec k) = 1` of the source into `b ∘ a = 1` and gives `a ∘ b = [Γ_{X → x → X}] = c₀`,
> so `c₀` splits through `Spec k` and `a`, `b` are mutually inverse morphisms of motives.

```lean
def constantGraphMotiveIso {P Q : D} (α : P ⟶ Q) (β : Q ⟶ P) (hαβ : α ≫ β = 𝟙 P) :
    S.constantGraphMotive α β hαβ ≅ S.motiveFunctor.obj P
```

## Tag 0FGE, a remark

[Tag 0FGE](https://stacks.math.columbia.edu/tag/0FGE) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.lefschetzMotive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotive.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotive.lean#L67). The attribute's comment: “the Lefschetz motive (X, c\_2, 0) in M\_k for X = P^1\_k and c\_2 as in 0FG6, written L, bold L, Q(-1) or h^2(P^1\_k)”.

> The *Lefschetz motive* `(P¹_k, c₂, 0)`: the projective line, cut down by the projector
> `c₂ = [P¹_k × x]` of Example 0FG6 attached to a `k`-rational point `x`, with no twist, as an
> object of the category `M_k` of Chow motives. In the literature it is denoted `L`, `𝐋`, `𝐐(-1)`
> or `h²(P¹_k)`. Its invertibility, the content of Remark 0FGE, is
> `Stacks.WeilCohomology.ChowMotiveCat.isInvertible_lefschetzMotive`.

```lean
def lefschetzMotive : ChowMotiveCat k
```

**`Stacks.WeilCohomology.ChowMotiveCat.lefschetzMotiveHasInverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotiveInvertible.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotiveInvertible.lean#L66). The attribute's comment: “the Lefschetz motive (P^1\_k, c\_2, 0) is invertible in M\_k, with inverse the Tate motive 1(1), via the isomorphism with 1(-1) of 0FGD; unconditional”.

> **Stacks Project, Tag 0FGE.** The Lefschetz motive `L = (P¹_k, c₂, 0)` is invertible in the
> symmetric monoidal category `M_k`, with inverse the Tate motive `1(1) = (Spec k, 1, 1)`: a
> two-sided tensor inverse `L ⊗ 1(1) ≅ 1`, `1(1) ⊗ L ≅ 1`, obtained by carrying the inverse
> `1(1)` of `1(-1)` along the isomorphism `L ≅ 1(-1)` of Lemma 0FGD.

```lean
def lefschetzMotiveHasInverse : HasInverse (lefschetzMotive x hx)
```

**`Stacks.WeilCohomology.ChowMotiveCat.lefschetzMotiveHasInverse_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotiveInvertible.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotiveInvertible.lean#L74). The attribute's comment: “the inverse of the Lefschetz motive is the Tate motive 1(1) = (Spec k, 1, 1)”.

> **Stacks Project, Tag 0FGE.** The inverse of the Lefschetz motive is the Tate motive
> `1(1) = (Spec k, 1, 1)`, also written `L⁻¹`, `𝐋⁻¹`, `𝐓` or `𝐐(1)`.

```lean
theorem lefschetzMotiveHasInverse_inv : (lefschetzMotiveHasInverse x hx).inv = tate k 1
```

**`Stacks.WeilCohomology.ChowMotiveCat.isInvertible_lefschetzMotive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotiveInvertible.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/LefschetzMotiveInvertible.lean#L80). The attribute's comment: “the Lefschetz motive is invertible in M\_k (Categories, Definition 0FFN)”.

> **Stacks Project, Tag 0FGE.** The Lefschetz motive is invertible in `M_k` in the sense of
> Categories, Definition 0FFN, for every field `k` and `k`-rational point `x` of `P¹_k`.

```lean
theorem isInvertible_lefschetzMotive : IsInvertible (lefschetzMotive x hx)
```

## Tag 0FGF, a lemma

[Tag 0FGF](https://stacks.math.columbia.edu/tag/0FGF) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.hasFiniteBiproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesFiniteBiproducts.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesFiniteBiproducts.lean#L82). The attribute's comment: “M\_k is additive: finite direct sums, via (Y ⨿ Z, p + q, m) for equal twists and (Z, q, n) ≅ (Z, q, m) ⊗ (P¹, c₂, 0)^\{⊗(m-n)}”.

> The category `M_k` of Chow motives is additive: it is preadditive (`ℚ`-linear, Stacks 0FGA)
> and has finite direct sums. A zero object is a motive with zero projector; two motives
> `(Y, p, m)`, `(Z, q, m)` with the same twist have the direct sum `(Y ⨿ Z, p + q, m)`; and a
> motive `(Z, q, n)` is isomorphic to `(Z, q, m) ⊗ (P¹_k, c₂, 0)^{⊗ (m - n)}`, of twist `m`, since
> `(P¹_k, c₂, 0) ≅ 𝟏(-1)`.

```lean
instance hasFiniteBiproducts : HasFiniteBiproducts (ChowMotiveCat k)
```

## Tag 0FGG, a lemma

[Tag 0FGG](https://stacks.math.columbia.edu/tag/0FGG) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.projectiveLineMotiveBiproductData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineMotive.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineMotive.lean#L129). The attribute's comment: “h(P^1\_k) is the direct sum of 1 and 1(-1) in M\_k: a bilimit bicone over 1 and 1(-1) with point h(P^1\_k), built from any k-rational point of the actual P^1\_k, in the actual category of Chow motives, with Example 0FG6 and Lemma 0FGD proved for it”.

> **Stacks Project, Tag 0FGG.** In `M_k` the motive `h(P¹_k)` is the direct sum of
> `1 = (Spec k, 1, 0)` and `1(-1) = (Spec k, 1, -1)`: a bilimit binary bicone over `1` and `1(-1)`
> whose point is `h(P¹_k)`, see
> `Stacks.WeilCohomology.ChowMotiveCat.projectiveLineMotiveBiproductData_bicone_pt`.
>
> It is obtained from the splitting `h(P¹_k) = (P¹_k, c₀, 0) ⊕ (P¹_k, c₂, 0)` by the projectors of
> Example 0FG6 attached to the `k`-rational point `x`, followed by the two isomorphisms
> `(P¹_k, c₀, 0) ≅ 1` and `(P¹_k, c₂, 0) ≅ 1(-1)` of Lemma 0FGD.

```lean
def projectiveLineMotiveBiproductData : BinaryBiproductData (tate k 0) (tate k (-1))
```

**`Stacks.WeilCohomology.ChowMotiveCat.projectiveLineMotiveIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineMotive.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineMotive.lean#L159). The attribute's comment: “in M\_k we have h(P^1\_k) iso 1 + 1(-1), for the actual P^1\_k and the actual category of Chow motives, with Example 0FG6 and Lemma 0FGD proved for P^1\_k”.

> **Stacks Project, Tag 0FGG.** In `M_k` we have `h(P¹_k) ≅ 1 ⊕ 1(-1)`.
>
> This is `Stacks.WeilCohomology.ChowMotiveCat.projectiveLineMotiveBiproductData`, at the rational
> point `∞` of `P¹_k`, compared with the chosen direct sum `1 ⊞ 1(-1)`, whose existence is
> `Stacks.WeilCohomology.ChowMotiveCat.hasBinaryBiproduct_tate_zero_tate_neg_one`. Nothing beyond
> the field `k` is assumed: the relations of Example 0FG6 and the isomorphisms of Lemma 0FGD are
> proved for `P¹_k`. The abstract form of the deduction, for an arbitrary category of
> correspondences, is `Stacks.WeilCohomology.CorrespondenceStructure.projectiveLineMotiveIso`.

```lean
def projectiveLineMotiveIso :
    (h k).obj (Opposite.op (projectiveLineObj k)) ≅ tate k 0 ⊞ tate k (-1)
```

## Tag 0FGH, a lemma

[Tag 0FGH](https://stacks.math.columbia.edu/tag/0FGH) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.universalProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesUniversalProperty.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotivesUniversalProperty.lean#L104). The attribute's comment: “a Q-linear symmetric monoidal functor F on degree-0 correspondences with the image of F(c₂) on F(P¹) invertible factors through M\_k, uniquely up to unique monoidal isomorphism”.

> **Stacks Project, Tag 0FGH.** Let `X = P¹_k`, `x` a rational point and `c₂ = [X × x]`
> (Example 0FG6). Let `𝒞` be a `ℚ`-linear Karoubian symmetric monoidal category. A `ℚ`-linear functor
> of symmetric monoidal categories `F` from the category of smooth projective schemes over `k` with
> correspondences of degree `0` to `𝒞`, such that the image of `F(c₂)` on `F(X)` is an invertible
> object, factors through a functor `G : M_k ⥤ 𝒞` of symmetric monoidal categories along
> `X ↦ (X, 1, 0)` — by a monoidal isomorphism, `G` being moreover additive and `ℚ`-linear — and the
> factorization is unique: any two are related by a unique monoidal isomorphism compatible with the
> identifications.
>
> This is the declaration registered for Stacks 0FGH; the Karoubi-envelope lemmas of
> `StacksFrontier.AlgebraicGeometry.WeilCohomology.Motives.UniversalProperty` are auxiliary.

```lean
theorem universalProperty {𝒞 : Type u₂} [Category.{v₂} 𝒞] [MonoidalCategory 𝒞]
    [SymmetricCategory 𝒞] [Preadditive 𝒞] [Linear ℚ 𝒞] [MonoidalPreadditive 𝒞]
    [IsIdempotentComplete 𝒞]
    (F : DegreeZero ℚ (CorrespondenceCategory k) ⥤ 𝒞) [F.Braided] [F.Additive]
    [Functor.Linear ℚ F]
    (hF : ∃ (U : 𝒞) (i : U ⟶ F.obj (projectiveLineDegreeZero k))
      (e : F.obj (projectiveLineDegreeZero k) ⟶ U),
      i ≫ e = 𝟙 U ∧ e ≫ i = F.map (projectiveLineFibrePointDegreeZero x hx) ∧ IsInvertible U) :
    (∃ (G : ChowMotiveCat k ⥤ 𝒞) (_ : G.Braided) (_ : G.Additive) (_ : Functor.Linear ℚ G)
        (φ : TwistedKaroubi.untwistedOfObj (CorrespondenceCategory k) ⋙ G ≅ F),
        NatTrans.IsMonoidal φ.hom) ∧
      ∀ (G₁ G₂ : ChowMotiveCat k ⥤ 𝒞) [G₁.Braided] [G₂.Braided]
        (φ₁ : TwistedKaroubi.untwistedOfObj (CorrespondenceCategory k) ⋙ G₁ ≅ F)
        (φ₂ : TwistedKaroubi.untwistedOfObj (CorrespondenceCategory k) ⋙ G₂ ≅ F)
        [NatTrans.IsMonoidal φ₁.hom] [NatTrans.IsMonoidal φ₂.hom],
        ∃! θ : G₁ ≅ G₂, NatTrans.IsMonoidal θ.hom ∧
          Functor.whiskerLeft (TwistedKaroubi.untwistedOfObj (CorrespondenceCategory k)) θ.hom ≫
            φ₂.hom = φ₁.hom
```

## Tag 0FGI, a lemma

[Tag 0FGI](https://stacks.math.columbia.edu/tag/0FGI) in the Stacks Project.

**`Stacks.WeilCohomology.motiveExactPairing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotiveDuality.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotiveDuality.lean#L106).

> **Stacks Project, Tag 0FGI.** Let `X` be a smooth projective scheme over `k` which is
> equidimensional of dimension `d`. Then `h(X)(d) = h(X) ⊗ 𝟏(d)` is a left dual of `h(X)` in the
> category `M_k` of Chow motives: there are `η : 𝟏 ⟶ h(X) ⊗ h(X)(d)` and
> `ε : h(X)(d) ⊗ h(X) ⟶ 𝟏`, both the class `[Δ]` of the diagonal, satisfying the two triangle
> identities (Categories, Definition 0FFP; Mathlib's `ExactPairing`). Equidimensionality of
> dimension `d` is `RelativeDimension X.obj.hom d`; `X` may be empty.

```lean
def motiveExactPairing (hX : RelativeDimension X.obj.hom d) :
    ExactPairing ((ChowMotiveCat.h k).obj (op X))
      ((ChowMotiveCat.h k).obj (op X) ⊗ ChowMotiveCat.tate k d)
```

**`Stacks.WeilCohomology.nonempty_exactPairing_motive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotiveDuality.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/MotiveDuality.lean#L116).

> **Stacks 0FGI**, as a statement: `h(X)` has `h(X)(d)` as a left dual in `M_k`.

```lean
theorem nonempty_exactPairing_motive (hX : RelativeDimension X.obj.hom d) :
    Nonempty (ExactPairing ((ChowMotiveCat.h k).obj (op X))
      ((ChowMotiveCat.h k).obj (op X) ⊗ ChowMotiveCat.tate k d))
```

**`Stacks.WeilCohomology.selfCorrespondenceEquivCoevaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Duality.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Duality.lean#L116). The attribute's comment: “the identification Corr^0(X,X) = Corr^d(Spec k, X x X) = CH^d(X x X) tensor Q, which puts the identity [D] of h(X) and the unit of the duality in one group”.

> For `X` equidimensional of dimension `d`, so that `X × X` is
> equidimensional of dimension `2 * d`, the canonical `ℚ`-linear isomorphism
>
>   `Corr⁰(X, X) = CH^d(X × X) ⊗ ℚ = Corr^d(Spec k, X × X)`.
>
> The left-hand group is `Hom(h(X), h(X))`, which contains the identity `[Δ]`; the right-hand one
> is `Hom(1, h(X) ⊗ h(X)(d))`, which contains the unit `η` of the duality. The identification is
> that of Tag 0FG0 (3), proper pushforward along the collapsing projection
> `Spec k × (X × X) ≅ X × X`.

```lean
def selfCorrespondenceEquivCoevaluation :
    Correspondence C sX sX d 0 ≃ₗ[ℚ]
      Correspondence C (𝟙 C.S) (pullback.fst sX sX ≫ sX) (2 * d) d
```

**`Stacks.WeilCohomology.selfCorrespondenceEquivEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Duality.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Duality.lean#L134). The attribute's comment: “the identification Corr^0(X,X) = Corr^\{-d}(X x X, Spec k) = CH\_d(X x X) tensor Q, which puts the identity [D] of h(X) and the counit of the duality in one group”.

> For `X` equidimensional of dimension `d` the canonical
> `ℚ`-linear isomorphism
>
>   `Corr⁰(X, X) = CH_d(X × X) ⊗ ℚ = Corr^{-d}(X × X, Spec k)`.
>
> The right-hand group is `Hom(h(X)(d) ⊗ h(X), 1)`, which contains the counit `ε` of the duality.
> The identification is that of Tag 0FG0 (2), proper pushforward along the collapsing projection
> `(X × X) × Spec k ≅ X × X`.

```lean
def selfCorrespondenceEquivEvaluation :
    Correspondence C sX sX d 0 ≃ₗ[ℚ]
      Correspondence C (pullback.fst sX sX ≫ sX) (𝟙 C.S) 0 (-d)
```

**`Stacks.WeilCohomology.dualityCorrespondenceEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Duality.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Duality.lean#L148). The attribute's comment: “the identification Corr^d(Spec k, X x X) = Corr^\{-d}(X x X, Spec k) that makes one class [D] serve as identity, as unit and as counit”.

> The group of candidate units of the duality and the group of
> candidate counits are canonically the same, both being `CH^d(X × X) ⊗ ℚ = CH_d(X × X) ⊗ ℚ`:
>
>   `Corr^d(Spec k, X × X) = Corr^{-d}(X × X, Spec k)`.

```lean
def dualityCorrespondenceEquiv :
    Correspondence C (𝟙 C.S) (pullback.fst sX sX ≫ sX) (2 * d) d ≃ₗ[ℚ]
      Correspondence C (pullback.fst sX sX ≫ sX) (𝟙 C.S) 0 (-d)
```

## Tag 0FGJ, a lemma

[Tag 0FGJ](https://stacks.math.columbia.edu/tag/0FGJ) in the Stacks Project.

**`Stacks.WeilCohomology.ChowMotiveCat.rightRigidCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Rigid.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Rigid.lean#L82).

> **Stacks 0FGJ.** Every object of the category `M_k` of Chow motives has a left dual:
> `M_k` is (right) rigid, in Mathlib's naming.

```lean
noncomputable instance rightRigidCategory : RightRigidCategory (ChowMotiveCat k)
```

**`Stacks.WeilCohomology.ChowMotiveCat.nonempty_hasRightDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Rigid.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/Rigid.lean#L89).

> **Stacks 0FGJ**, objectwise: every Chow motive `M` has a left dual (Stacks' "`Mᘁ` is a left
> dual of `M`" is Mathlib's `ExactPairing M Mᘁ`).

```lean
theorem nonempty_hasRightDual (M : ChowMotiveCat k) : Nonempty (HasRightDual M)
```

**`Stacks.WeilCohomology.rightRigidCategoryOfRetractTwist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Rigidity.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Motives/Rigidity.lean#L186). The attribute's comment: “every object of M\_k has a left dual, i.e. M\_k is right rigid in Mathlib's naming. STATED IN AN ABSTRACT MONOIDAL CATEGORY, not on this library's category of motives, because the monoidal structure on Karoubi S.Obj is Stacks 0FGC, which is not yet formalized in this repository, so the twist h(X)(m) = h(X) tensor 1(m) cannot be written on `S.Motive` at all. The statement specialises to the source's setting as soon as 0FGC is formalized, and h : D → Mot is kept untwisted on purpose, the Tate objects being supplied separately as T : Z → Mot, exactly as in the 0FGN statement of ManinIdentityPrinciple whose `hdual` hypothesis this discharges. Three pieces of data are carried rather than used, each named in the signature: Stacks 0FGI that h(X) has a left dual (hh), which this repository does prove from DiagonalPairingData and which rightRigidCategoryOfDiagonalPairingData feeds in; invertibility of the Tate motive, that 1(m) is a left dual of 1(-m) in the Stacks 0FFP sense (hT); and generation, that every motive is a retract of a twist h(X)(m) (hgen), taken in the weak Retract sense so the theorem is stronger. Karoubianness of M\_k is the typeclass IsIdempotentComplete. Reused rather than reproved: Stacks 0FFS as Mathlib's hasRightDualTensor and Stacks 0FFU as this library's nonempty\_hasRightDual\_of\_retract”.

> **Stacks Project, Tag 0FGJ.** Every object of the category `M_k` of motives has a left dual,
> i.e. `M_k` is a rigid category.
>
> Here `Mot` is the category `M_k` of motives of Stacks 0FGA, monoidal by Stacks 0FGC, `h X` is the
> motive of a smooth projective scheme `X` over `k`, and `T m` is the Tate object `1(m)`. The
> hypothesis `hh` is Stacks 0FGI, that `h(X)` has a left dual — supplied from this repository's
> own 0FGI by `Stacks.WeilCohomology.rightRigidCategoryOfDiagonalPairingData` below; `hT` is the
> invertibility of the Tate motive, that `1(m)` is a left dual of `1(-m)`; and `hgen` says that
> every motive is a direct summand of a twist `h(X)(m)`. See the implementation notes of this file
> for why each is carried rather than used.

```lean
def rightRigidCategoryOfRetractTwist (h : D → Mot) (hh : ∀ X : D, HasRightDual (h X))
    (T : ℤ → Mot) (hT : ∀ m : ℤ, ExactPairing (T (-m)) (T m))
    (hgen : ∀ L : Mot, ∃ (X : D) (m : ℤ), Nonempty (Retract L (h X ⊗ T m))) :
    RightRigidCategory Mot
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.4, Tag 0FG9](https://stacks.math.columbia.edu/tag/0FG9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
