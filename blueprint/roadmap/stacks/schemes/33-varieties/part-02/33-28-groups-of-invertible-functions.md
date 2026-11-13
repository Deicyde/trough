---
declaration: section
origin: cited
lean: AlgebraicGeometry.fg_units_quotient_of_isOpenImmersion_into_properVariety, AlgebraicGeometry.fg_units_quotient_of_locallyOfFiniteType, AlgebraicGeometry.fg_units_quotient_of_connectedSpace_of_isReduced, AlgebraicGeometry.integralClosure_globalSections_isField, AlgebraicGeometry.fg_units_quotient_of_integrallyClosed, AlgebraicGeometry.fg_units_quotient_of_rationalPoint, AlgebraicGeometry.fg_units_quotient_of_geometricallyIntegral, AlgebraicGeometry.integralClosure_globalSections_eq_bot_of_isAlgClosedIn_functionField
statement: formalized
proof: formalized
---

# 33.28 Groups of invertible functions

Section 33.28 of the Stacks Project, [Tag 04L3](https://stacks.math.columbia.edu/tag/04L3). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04L4, a lemma

[Tag 04L4](https://stacks.math.columbia.edu/tag/04L4) in the Stacks Project.

**`AlgebraicGeometry.fg_units_quotient_of_isOpenImmersion_into_properVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/NormalModel.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/NormalModel.lean#L44).

> **Stacks Project, Tag 04L4.** Let `k` be an algebraically closed field, let `Xbar` be a
> proper variety over `k`, and let `X` be a normal open subscheme of `Xbar`. Then the group of
> invertible global functions on `X`, modulo the constants coming from `k`, is finitely generated.
>
> The ambient proper variety may be replaced by its normalization, which is again a proper variety
> over `k` and is normal, and over the normal open `X` the normalization morphism is an
> isomorphism; so the statement follows from the case of a normal ambient variety.

```lean
theorem fg_units_quotient_of_isOpenImmersion_into_properVariety
    (k : Type u) [Field k] [IsAlgClosed k] {X Xbar : Scheme.{u}}
    (f : Xbar ⟶ Spec (.of k)) [IsProperVariety k f]
    (i : X ⟶ Xbar) [IsOpenImmersion i] [IsNormal X] :
    let φ : k →+* Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ (i ≫ f).appTop).hom
    Group.FG (Units Γ(X, ⊤) ⧸ (Units.map φ.toMonoidHom).range)
```

## Tag 04L5, a lemma

[Tag 04L5](https://stacks.math.columbia.edu/tag/04L5) in the Stacks Project.

**`AlgebraicGeometry.fg_units_quotient_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/FiniteType.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/FiniteType.lean#L178).

> **Stacks Project, Tag 04L5.** Let `k` be an algebraically closed field and let `X` be an
> integral scheme locally of finite type over `k`.  Then the group of invertible global functions on
> `X` modulo the constants coming from `k` is a finitely generated abelian group.
>
> The normalization `ν : X^ν ⟶ X` is finite, `X^ν` is a normal integral scheme locally of finite
> type over `k`, and `ν` is dominant, hence injective on global sections; so the statement follows
> from the normal case.

```lean
theorem fg_units_quotient_of_locallyOfFiniteType (k : Type u) [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} [IsIntegral X] (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    let φ : k →+* Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom
    Group.FG (Γ(X, ⊤)ˣ ⧸ (Units.map φ.toMonoidHom).range)
```

## Tag 04L6, a lemma

[Tag 04L6](https://stacks.math.columbia.edu/tag/04L6) in the Stacks Project.

**`AlgebraicGeometry.fg_units_quotient_of_connectedSpace_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReduced.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReduced.lean#L228).

> Let `k` be an algebraically closed field and let `X` be a connected reduced scheme which is
> locally of finite type over `k` and has finitely many irreducible components.  Then `𝒪^*(X)/k^*`,
> the group of invertible global functions on `X` modulo the constants coming from `k`, is a finitely
> generated abelian group.

```lean
theorem fg_units_quotient_of_connectedSpace_of_isReduced (k : Type u) [Field k] [IsAlgClosed k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [ConnectedSpace X] [IsReduced X]
    [LocallyOfFiniteType f] (hX : (irreducibleComponents (X : Type u)).Finite) :
    Group.FG (Γ(X, ⊤)ˣ ⧸ (Units.map
      (((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom).toMonoidHom).range)
```

## Tag 04MI, a lemma

[Tag 04MI](https://stacks.math.columbia.edu/tag/04MI) in the Stacks Project.

**`AlgebraicGeometry.integralClosure_globalSections_isField`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/GlobalSections.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Defs/GlobalSections.lean#L49).

> The integral closure of the ground field in the global sections of a
> connected reduced scheme over that field is a field.

```lean
public lemma integralClosure_globalSections_isField
    (k : Type u) [Field k] (X : Scheme.{u})
    (f : X ⟶ Spec (.of k)) [ConnectedSpace X] [IsReduced X] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    IsField (integralClosure k Γ(X, ⊤))
```

## Tag 04L7, a proposition

[Tag 04L7](https://stacks.math.columbia.edu/tag/04L7) in the Stacks Project.

**`AlgebraicGeometry.fg_units_quotient_of_integrallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReducedBaseChange.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReducedBaseChange.lean#L234). The attribute's comment: “integral\_closure\_of\_ground\_field\_is\_ground\_field”.

> **Stacks Project, Tag 04L7 under its condition (1).** Let `k` be a field and let `X` be a
> connected reduced scheme, locally of finite type over `k`, with finitely many irreducible
> components, and assume that every global section of `X` integral over `k` is a constant — that is,
> that the integral closure of `k` in `Γ(X, 𝒪_X)` is `k`.  Then the group of invertible global
> functions on `X` modulo the constants coming from `k` is a finitely generated abelian group.
>
> The base change `X̄ = X ×_k \bar k` is surjective over `X` and has finitely many irreducible
> components; each of them with its reduced induced structure is integral and locally of finite type
> over `\bar k`, so Tag 04L5 applies to it.  A unit of `Γ(X, 𝒪_X)` which is a constant from
> `\bar k` on every component of `X̄` is killed by the product of the minimal polynomials of those
> constants over `k`, hence is integral over `k`, hence is a constant from `k` by the hypothesis.
>
> Connectedness of `X` is one of the source's hypotheses and is kept here, but this proof does not
> use it: in the source connectedness is what forces the constants on the components to agree,
> whereas here condition (1) does that work.

```lean
theorem fg_units_quotient_of_integrallyClosed (k : Type u) [Field k] (X : Scheme.{u})
    (f : X ⟶ Spec (.of k)) [ConnectedSpace X] [IsReduced X] [LocallyOfFiniteType f]
    (hX : (irreducibleComponents (X : Type u)).Finite)
    (h1 : ∀ a : Γ(X, ⊤), (((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom).IsIntegralElem a →
      a ∈ Set.range ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom) :
    Group.FG (Γ(X, ⊤)ˣ ⧸ (Units.map
      (((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom).toMonoidHom).range)
```

**`AlgebraicGeometry.fg_units_quotient_of_rationalPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReducedBaseChange.lean, line 438](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReducedBaseChange.lean#L438). The attribute's comment: “rational\_point”.

> **Stacks Project, Tag 04L7 under its condition (2).** Let `k` be a field and let `X` be a
> connected reduced scheme, locally of finite type over `k`, with finitely many irreducible
> components, and suppose `X` has a `k`-rational point.  Then the group of invertible global
> functions on `X` modulo the constants coming from `k` is a finitely generated abelian group.
>
> Condition (2) implies condition (1) by `mem_range_of_isIntegralElem_of_rationalPoint`, which is
> the source's own argument.

```lean
theorem fg_units_quotient_of_rationalPoint (k : Type u) [Field k] (X : Scheme.{u})
    (f : X ⟶ Spec (.of k)) [ConnectedSpace X] [IsReduced X] [LocallyOfFiniteType f]
    (hX : (irreducibleComponents (X : Type u)).Finite) (e : Spec (.of k) ⟶ X)
    (he : e ≫ f = 𝟙 (Spec (.of k))) :
    Group.FG (Γ(X, ⊤)ˣ ⧸ (Units.map
      (((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom).toMonoidHom).range)
```

**`AlgebraicGeometry.fg_units_quotient_of_geometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReducedGeometricallyIntegral.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/ConnectedReducedGeometricallyIntegral.lean#L92). The attribute's comment: “geometrically\_integral”.

> **Stacks Project, Tag 04L7 under its condition (3).** Let `k` be a field and let `X` be a
> connected reduced scheme, locally of finite type over `k`, with finitely many irreducible
> components, and suppose `X` is geometrically integral over `k`.  Then the group of invertible
> global functions on `X` modulo the constants coming from `k` is a finitely generated abelian
> group.
>
> Condition (3) implies condition (1) by `mem_range_of_isIntegralElem_of_geometricallyIntegral`, and
> `fg_units_quotient_of_integrallyClosed` is the proposition under condition (1).

```lean
theorem fg_units_quotient_of_geometricallyIntegral (k : Type u) [Field k] (X : Scheme.{u})
    (f : X ⟶ Spec (.of k)) [ConnectedSpace X] [IsReduced X] [LocallyOfFiniteType f]
    (hX : (irreducibleComponents (X : Type u)).Finite) (hgi : GeometricallyIntegral f) :
    Group.FG (Γ(X, ⊤)ˣ ⧸ (Units.map
      (((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom).toMonoidHom).range)
```

## Tag 04L8, a lemma

[Tag 04L8](https://stacks.math.columbia.edu/tag/04L8) in the Stacks Project.

**`AlgebraicGeometry.integralClosure_globalSections_eq_bot_of_isAlgClosedIn_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean#L149). The attribute's comment: “condition (2) implies condition (1); the source omits this verification”.

> **Stacks Project, Tag 04L8, condition (2) implies condition (1).** Let `k` be a field and let
> `X` be an integral scheme over `k`.  If `k` is algebraically closed in the function field of `X`,
> then the integral closure of `k` in `Γ(X, 𝒪_X)` is `k`.
>
> The germ map from the global sections to the stalk at the generic point is injective on an
> integral scheme, so this is the field-theoretic statement
> `integralClosure_eq_bot_of_isAlgClosedIn_of_injective`.

```lean
theorem integralClosure_globalSections_eq_bot_of_isAlgClosedIn_functionField
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsIntegral X] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    letI : Algebra k X.functionField :=
      ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫
        X.presheaf.germ ⊤ (genericPoint X) trivial).hom.toAlgebra
    IsAlgClosedIn k X.functionField → integralClosure k Γ(X, ⊤) = ⊥
```

**`AlgebraicGeometry.integralClosure_globalSections_eq_bot_of_closedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean#L176). The attribute's comment: “condition (4) implies condition (1); the source omits this verification”.

> **Stacks Project, Tag 04L8, condition (4) implies condition (1).** Let `k` be a field and let
> `X` be a connected reduced scheme over `k`.  Suppose that every field extension `L` of `k` which
> admits at each closed point `x` of `X` a ring map to the residue field `κ(x)` compatible with the
> maps out of `k` is already equal to `k`.  Then the integral closure of `k` in `Γ(X, 𝒪_X)` is `k`.
>
> The integral closure is a field by Tag 04MI, and evaluation at a point restricts to a ring map
> from it to the residue field there which is compatible with the maps out of `k`.  So the
> hypothesis applies to it and makes it `k`.

```lean
theorem integralClosure_globalSections_eq_bot_of_closedPoints
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [ConnectedSpace X] [IsReduced X] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    (∀ (L : Type u) [Field L] [Algebra k L],
      (∀ x ∈ closedPoints X, ∃ ι : L →+* X.residueField x,
        ∀ a : k, ι (algebraMap k L a) = X.Γevaluation x (algebraMap k Γ(X, ⊤) a)) →
      Function.Surjective (algebraMap k L)) →
    integralClosure k Γ(X, ⊤) = ⊥
```

**`AlgebraicGeometry.integralClosure_globalSections_eq_bot_of_geometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean#L231). The attribute's comment: “condition (3) implies condition (1); the source omits this verification”.

> **Stacks Project, Tag 04L8, condition (3) implies condition (1).** Let `k` be a field and let
> `X` be an integral scheme over `k` which is geometrically integral.  Then the integral closure of
> `k` in `Γ(X, 𝒪_X)` is `k`.
>
> Geometric integrality is geometric reducedness together with geometric irreducibility.  The first
> says the function field is a separable extension of `k` (Tag 04KS) and the second says `k` is
> separably closed in the residue field at the generic point (Tag 054Q), which is the same field;
> so `k` is algebraically closed in the function field, which is condition (2).

```lean
theorem integralClosure_globalSections_eq_bot_of_geometricallyIntegral
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsIntegral X]
    (hgi : GeometricallyIntegral f) :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    integralClosure k Γ(X, ⊤) = ⊥
```

**`AlgebraicGeometry.fg_units_quotient_of_isVariety_of_field_conditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/InvertibleFunctions/VarietyFieldConditions.lean#L279).

> **Stacks Project, Tag 04L8.** Let `k` be a field and let `X` be a variety over `k`.  Then the
> group of invertible global functions on `X` modulo the constants coming from `k` is finitely
> generated as soon as one of the following holds: the integral closure of `k` in `Γ(X, 𝒪_X)` is
> `k`; `k` is algebraically closed in the function field of `X`; `X` is geometrically integral over
> `k`; or no field extension of `k` other than `k` itself admits at every closed point a map to the
> residue field there compatible with the maps out of `k`.
>
> A variety is integral, hence connected and reduced with a single irreducible component, and its
> structure morphism is locally of finite type, so Proposition 04L7 under its condition (1) —
> `AlgebraicGeometry.fg_units_quotient_of_integrallyClosed` — applies.  Each of the other three
> conditions is turned into condition (1) by the three lemmas above.

```lean
theorem fg_units_quotient_of_isVariety_of_field_conditions
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsVariety k f] :
    letI : Algebra k Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom.toAlgebra
    (integralClosure k Γ(X, ⊤) = ⊥ ∨
      (letI : Algebra k X.functionField :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫
          X.presheaf.germ ⊤ (genericPoint X) trivial).hom.toAlgebra
       IsAlgClosedIn k X.functionField) ∨
      GeometricallyIntegral f ∨
      (∀ (L : Type u) [Field L] [Algebra k L],
        (∀ x ∈ closedPoints X, ∃ ι : L →+* X.residueField x,
          ∀ a : k, ι (algebraMap k L a) = X.Γevaluation x (algebraMap k Γ(X, ⊤) a)) →
        Function.Surjective (algebraMap k L))) →
    Group.FG (Γ(X, ⊤)ˣ ⧸ (Units.map
      (((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop).hom).toMonoidHom).range)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.28, Tag 04L3](https://stacks.math.columbia.edu/tag/04L3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
