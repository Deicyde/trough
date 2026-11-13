---
declaration: section
origin: cited
lean: Stacks.Divisors.fiber_support_eq_union_irreducibleComponents_general, Stacks.Divisors.fiber_support_eq_union_irreducibleComponents, IsLocalRing.injective_quotient_of_dimension_add_trdeg_eq, IsLocalRing.ringKrullDim_closedFiber_add_trdeg_eq_trdeg, AlgebraicGeometry.closure_closedPoints_between_fiber_eq_iff, AlgebraicGeometry.exists_chain_isImmediateSpecialization_isClosed_fiber, AlgebraicGeometry.natTrdegFiber_eq_topologicalKrullDim_closure, AlgebraicGeometry.natTrdegFiber_eq_toNat_trdeg_residueField
statement: formalized
proof: formalized
---

# 37.52 Closed points in fibres

Section 37.52 of the Stacks Project, [Tag 053Q](https://stacks.math.columbia.edu/tag/053Q). 9 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 053R, a lemma

[Tag 053R](https://stacks.math.columbia.edu/tag/053R) in the Stacks Project.

**`Stacks.Divisors.fiber_support_eq_union_irreducibleComponents_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimension/GeneralCase.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FibreDimension/GeneralCase.lean#L355).

> **Stacks 053R.** Let `f : X ⟶ S` be a dominant morphism locally of finite type between
> irreducible schemes, let `I` be a locally principal ideal sheaf on `X` whose closed subscheme
> misses the generic fibre of `f`, and let `s` be a point of `S` whose fibre has dimension at most
> that of the generic fibre. Then the support of the closed subscheme inside the fibre `X_s` is
> set-theoretically the union of the irreducible components of `X_s` that it contains.
>
> No Noetherian hypothesis: the Noetherian case
> `Stacks.Divisors.fiber_support_eq_union_irreducibleComponents` is applied not to `f` but to a
> finitely generated `ℤ`-algebra that the affine situation descends to, in
> `Stacks.Divisors.fiber_preimage_zeroLocus_eq_sUnion_irreducibleComponents`. The two reductions in
> front of that are
> `Stacks.Divisors.fiber_support_eq_union_irreducibleComponents_of_isIntegral`, which passes to the
> reductions of `X` and `S` and so makes both integral, and
> `Stacks.Divisors.fiber_support_eq_union_irreducibleComponents_integral`, which localises to an
> affine chart on which `I` is principal.

```lean
public theorem fiber_support_eq_union_irreducibleComponents_general {X S : Scheme.{u}}
    (f : X ⟶ S) [IrreducibleSpace S] [IrreducibleSpace X] [IsDominant f] [LocallyOfFiniteType f]
    (I : X.IdealSheafData) (hI : IsLocallyPrincipal I)
    (hgeneric : IsEmpty ((I.subschemeι ≫ f).fiber (genericPoint S))) (s : S)
    (hdim : topologicalKrullDim (f.fiber s) ≤ topologicalKrullDim (f.fiber (genericPoint S))) :
    (f.fiberι s) ⁻¹' (I.support : Set X) =
      ⋃₀ {C : Set (f.fiber s) | C ∈ irreducibleComponents (f.fiber s) ∧
        C ⊆ (f.fiberι s) ⁻¹' (I.support : Set X)}
```

**`Stacks.Divisors.fiber_support_eq_union_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/LocallyPrincipalSupport.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/LocallyPrincipalSupport.lean#L180). The attribute's comment: “the locally Noetherian case, the form in which Krull's principal ideal theorem applies to `f` directly. The statement without `[IsLocallyNoetherian X]`, which is the source's own, is `Stacks.Divisors.fiber_support_eq_union_irreducibleComponents_general` in `StacksFrontier/AlgebraicGeometry/FibreDimension/GeneralCase.lean:352`; it applies this one to a finitely generated ℤ-algebra that the affine situation descends to, by `StacksFrontier.AlgebraicGeometry.FibreDimension.AffineGeneralCase`.”.

> **Stacks 053R, the Noetherian case.** Let `f : X ⟶ S` be a dominant morphism locally of
> finite type between irreducible schemes with `X` locally Noetherian, let `I` be a locally
> principal ideal sheaf on `X` whose closed subscheme misses the generic fibre, and let `s ∈ S` be
> a point whose fibre has dimension at most that of the generic fibre. Then the support of the
> closed subscheme inside `f.fiber s` is set-theoretically the union of the irreducible components
> of `f.fiber s` that it contains.

```lean
public theorem fiber_support_eq_union_irreducibleComponents {X S : Scheme.{u}} (f : X ⟶ S)
    [IrreducibleSpace S] [IrreducibleSpace X] [IsDominant f] [LocallyOfFiniteType f]
    [IsLocallyNoetherian X] (I : X.IdealSheafData) (hI : IsLocallyPrincipal I)
    (hgeneric : IsEmpty ((I.subschemeι ≫ f).fiber (genericPoint S))) (s : S)
    (hdim : topologicalKrullDim (f.fiber s) ≤
      topologicalKrullDim (f.fiber (genericPoint S))) :
    (f.fiberι s) ⁻¹' (I.support : Set X) =
      ⋃₀ {C : Set (f.fiber s) | C ∈ irreducibleComponents (f.fiber s) ∧
        C ⊆ (f.fiberι s) ⁻¹' (I.support : Set X)}
```

## Tag 053S, a lemma

[Tag 053S](https://stacks.math.columbia.edu/tag/053S) in the Stacks Project.

**`IsLocalRing.injective_quotient_of_dimension_add_trdeg_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/HorizontalDivisor.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RelativeDimension/HorizontalDivisor.lean#L471).

> **Stacks 053S.** Let `A ⊆ B` be an injective local homomorphism of local domains with `B`
> essentially of finite type over `A`, and let `g ∈ 𝔪_B` lie in no minimal prime over `𝔪_A B`. If
> `dim (B/𝔪_A B) + trdeg_{κ(𝔪_A)} κ(𝔪_B) = trdeg_A B`, then `A → B/gB` is injective, i.e. the
> generic point of `Spec A` is in the image of `Spec (B/gB) → Spec A`.

```lean
public theorem injective_quotient_of_dimension_add_trdeg_eq
    {A B : Type u} [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsLocalRing A] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)]
    (hinj : Function.Injective (algebraMap A B))
    (hB : IsEssentiallyOfFiniteType A B (algebraMap A B))
    (g : B) (hg : g ∈ maximalIdeal B)
    (hnot : ∀ q ∈ (Ideal.map (algebraMap A B) (maximalIdeal A)).minimalPrimes, g ∉ q)
    (hdim : letI := (ResidueField.map (algebraMap A B)).toAlgebra;
      ringKrullDim (B ⧸ Ideal.map (algebraMap A B) (maximalIdeal A)) +
        (Cardinal.toENat (Algebra.trdeg (ResidueField A) (ResidueField B)) :
          WithBot ℕ∞) =
      (Cardinal.toENat (Algebra.trdeg A B) : WithBot ℕ∞)) :
    Function.Injective ((Ideal.Quotient.mk (Ideal.span {g})).comp (algebraMap A B))
```

## Tag 053T, a lemma

[Tag 053T](https://stacks.math.columbia.edu/tag/053T) in the Stacks Project.

**`IsLocalRing.ringKrullDim_closedFiber_add_trdeg_eq_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/FlatLocalExtension.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/RelativeDimension/FlatLocalExtension.lean#L399). References: EGA IV (5.5.7), “field base”.

> The dimension of the closed fibre of an injective flat essentially finite type local
> extension of domains, plus the residue-field transcendence degree, is the transcendence
> degree of the extension.

```lean
public theorem ringKrullDim_closedFiber_add_trdeg_eq_trdeg
    {A B : Type u} [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsLocalRing A] [IsLocalRing B] [Algebra A B]
    [IsLocalHom (algebraMap A B)]
    (hinj : Function.Injective (algebraMap A B))
    (hfinite : IsEssentiallyOfFiniteType A B (algebraMap A B))
    [Module.Flat A B] :
    letI := (IsLocalRing.ResidueField.map (algebraMap A B)).toAlgebra
    ringKrullDim (B ⧸ (IsLocalRing.maximalIdeal A).map (algebraMap A B)) +
      (Cardinal.toENat (Algebra.trdeg (IsLocalRing.ResidueField A)
        (IsLocalRing.ResidueField B)) : WithBot ℕ∞) =
      (Cardinal.toENat (Algebra.trdeg A B) : WithBot ℕ∞)
```

## Tag 053U, a lemma

[Tag 053U](https://stacks.math.columbia.edu/tag/053U) in the Stacks Project.

**`AlgebraicGeometry.closure_closedPoints_between_fiber_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ClosedPointsBetweenInFibres.lean, line 1752](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ClosedPointsBetweenInFibres.lean#L1752). The attribute's comment: “the density conclusion of the tag, under the tag's own hypotheses — `f` locally of finite type, `x ⤳ x'`, `x'` closed in `X_{f x'}` — together with its exact range of validity: the points of `X_s` closed in `X_s` and lying between `x` and `x'` are dense in the closure of `x` in `X_s` if and only if `x = x'` or `f x ≠ f x'`. The reverse implication is the tag itself, proved by the argument of the source in `closure_closedPoints_between_fiber_eq`; the forward implication disposes of the only remaining situation, a nontrivial specialization inside one fibre, where the tag's set is the single closed point `x'` and the density is false — a gap in the source's statement, computed in `closure_closedPoints_between_fiber_subset_singleton_of_eq_base` and respected by the source's own proof.”.

> **Stacks 053U**, under the hypotheses of the tag and no others. Let `f : X ⟶ S` be locally
> of finite type, let `x ⤳ x'` be a specialization in `X` with `x'` closed in its fibre
> `X_{f x'}`, and set `s = f x`. Then the points of `X_s` which are closed in `X_s` and lie
> between `x` and `x'` are dense in the closure of `x` in `X_s` if and only if `x = x'` or
> `f x ≠ f x'`.
>
> The reverse implication is the assertion of the tag and carries its mathematical content: it is
> `AlgebraicGeometry.closure_closedPoints_between_fiber_eq`, proved by the argument of the source.
>
> The forward implication settles the one remaining situation, a nontrivial specialization inside
> one fibre, where the density fails: a point of `X_s` closed in `X_s` which specializes to `x'`
> *is* `x'`, so the set of the tag is `{x'}`, whose closure is `{x'}`, while the closure of `x` in
> `X_s` is larger whenever `x ≠ x'` — for `X = 𝔸¹` over a field with `x` its generic point and
> `x'` a closed point it is all of `𝔸¹`. The implication is exactly that computation, through
> `AlgebraicGeometry.closure_closedPoints_between_fiber_subset_singleton_of_eq_base`. Since the
> source relates `f x` and `f x'` by no hypothesis, its statement overreaches there; its proof
> does not, drawing the same line at the prime-avoidance step (see the module docstring).

```lean
public theorem closure_closedPoints_between_fiber_eq_iff
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (x x' : X) (hxx' : x ⤳ x')
    (hx' : IsClosed ({f.asFiber x'} : Set (f.fiber (f x')))) :
    closure {y : f.fiber (f x) |
          IsClosed ({y} : Set (f.fiber (f x))) ∧
            x ⤳ ((f.fiberι (f x)) y) ∧
              ((f.fiberι (f x)) y) ⤳ x'} =
        closure ({f.asFiber x} : Set (f.fiber (f x))) ↔
      x = x' ∨ f x ≠ f x'
```

## Tag 053V, a remark

[Tag 053V](https://stacks.math.columbia.edu/tag/053V) in the Stacks Project.

**`AlgebraicGeometry.exists_chain_isImmediateSpecialization_isClosed_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainInFibre.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainInFibre.lean#L118). The attribute's comment: “the chain of immediate specializations inside the fibre, of length `d`, ending in a closed point of the fibre, together with the avoidance clause, and with nothing assumed about a prescribed `x'`. The final link `x_d ⤳ x'` to a prescribed `x'` with `x ⤳ x'` closed in its own fibre is not in this file, which never mentions `x'`; it is `AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber_of_isClosed` in `StacksFrontier.AlgebraicGeometry.Morphisms.Fibres.SpecializationChainToClosedSpecialization`, where `AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber_iff` states every assertion of the remark at once, at the hypotheses of the tag, together with the exact range of validity of the remark.”.

> **Stacks 053V**, the chain of immediate specializations inside the fibre, together with the
> avoidance clause. For `f` locally of finite type and `W` a closed subset of the fibre `X_{f x}`
> not containing `x`, there is a chain
>
> `x = c 0 ⤳ c 1 ⤳ ⋯ ⤳ c d`
>
> of `d = natTrdegFiber f x` immediate specializations inside `X_{f x}`, avoiding `W`, whose last
> term is a closed point of `X_{f x}`.

```lean
theorem exists_chain_isImmediateSpecialization_isClosed_fiber
    (f : X ⟶ S) [LocallyOfFiniteType f] (x : X)
    {W : Set (f.fiber (f x))} (hW : IsClosed W) (hxW : f.asFiber x ∉ W) :
    ∃ c : Fin (natTrdegFiber f x + 1) → f.fiber (f x),
      c 0 = f.asFiber x ∧
      (∀ i : Fin (natTrdegFiber f x),
        IsImmediateSpecialization (c i.castSucc) (c i.succ)) ∧
      IsClosed ({c (Fin.last (natTrdegFiber f x))} : Set (f.fiber (f x))) ∧
      ∀ i, c i ∉ W
```

**`AlgebraicGeometry.natTrdegFiber_eq_topologicalKrullDim_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainInFibre.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainInFibre.lean#L156). The attribute's comment: “the equality of `d` with the dimension of the closure of `x` in the fibre”.

> **Stacks 053V**, the identity `d = dim(closure of {x})`, the closure being taken in the
> fibre `X_{f x}`.

```lean
theorem natTrdegFiber_eq_topologicalKrullDim_closure (f : X ⟶ S) [LocallyOfFiniteType f]
    (x : X) :
    ((natTrdegFiber f x : ℕ∞) : WithBot ℕ∞) =
      topologicalKrullDim (closure ({f.asFiber x} : Set (f.fiber (f x))))
```

**`AlgebraicGeometry.natTrdegFiber_eq_toNat_trdeg_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainInFibre.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainInFibre.lean#L239). The attribute's comment: “the equality of the length `d` of the chain with the transcendence degree `trdeg_{κ(s)}(κ(x))`”.

> **Stacks 053V**, the identity `d = trdeg_{κ(s)}(κ(x))`: the integer produced by
> `AlgebraicGeometry.natTrdegFiber` is the transcendence degree of the residue field of `X` at `x`
> over the residue field of `S` at `s = f x`.

```lean
theorem natTrdegFiber_eq_toNat_trdeg_residueField (f : X ⟶ S) (x : X) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    natTrdegFiber f x =
      Cardinal.toNat (Algebra.trdeg (S.residueField (f x)) (X.residueField x))
```

**`AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainToClosedSpecialization.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainToClosedSpecialization.lean#L273). The attribute's comment: “the chain of immediate specializations inside the fibre, of length `d`, ending in a closed point of the fibre which specializes to the prescribed `x'` — unconditionally, the avoidance clause aside. The remark as a whole, avoidance clause included, is `AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber_iff` above, which states it at the hypotheses of the tag together with its exact range of validity”.

> **Stacks 053V without its avoidance clause**, and with no hypothesis added to the tag. For
> `f` locally of finite type and `x ⤳ x'` with `x'` closed in its own fibre there is a chain
>
> `x = c 0 ⤳ c 1 ⤳ ⋯ ⤳ c d`
>
> of `d = natTrdegFiber f x` immediate specializations inside `X_{f x}` whose last term is a closed
> point of `X_{f x}` specializing to `x'`.
>
> This needs no non-degeneracy hypothesis because the point to walk down to can be produced without
> Stacks 053U when `x'` already lies in the fibre of `x`: it is then `x'` itself. It is the
> avoidance clause that fails in that case, which is why the remark as a whole is registered on
> the equivalence
> `AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber_iff` above.

```lean
public theorem exists_chain_isImmediateSpecialization_specializes_fiber_of_isClosed
    (f : X ⟶ S) [LocallyOfFiniteType f] (x x' : X) (hxx' : x ⤳ x')
    (hx' : IsClosed ({f.asFiber x'} : Set (f.fiber (f x')))) :
    ∃ c : Fin (natTrdegFiber f x + 1) → f.fiber (f x),
      c 0 = f.asFiber x ∧
      (∀ i : Fin (natTrdegFiber f x),
        IsImmediateSpecialization (c i.castSucc) (c i.succ)) ∧
      IsClosed ({c (Fin.last (natTrdegFiber f x))} : Set (f.fiber (f x))) ∧
      f.fiberι (f x) (c (Fin.last (natTrdegFiber f x))) ⤳ x'
```

**`AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainToClosedSpecialization.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/SpecializationChainToClosedSpecialization.lean#L338). The attribute's comment: “EVERY assertion of the remark at once — the chain of `d` immediate specializations inside the fibre, its last term closed in the fibre, the final link `x_d ⤳ x'`, the avoidance of any closed subset of the fibre which misses `x`, and `d = natTrdegFiber f x` — under the tag's own hypotheses, namely `f` locally of finite type, `x ⤳ x'` and `x'` closed in `X_{f x'}`, together with its exact range of validity: all of that holds if and only if `x = x'` or `f x ≠ f x'`. The reverse implication is the remark itself, by the argument of the source in `exists_chain_isImmediateSpecialization_specializes_fiber`; the forward implication disposes of the one remaining situation, a nontrivial specialization inside a single fibre, where `{x'}` is a closed subset of the fibre missing `x` which the last term of the chain cannot avoid, since a closed point specializing to `x'` is `x'`. That is the gap inherited from Stacks 053U, recorded there in `closure_closedPoints_between_fiber_eq_iff`, and respected by the source's own proof.”.

> **Stacks 053V, under the hypotheses of the tag and no others.** Let `f : X ⟶ S` be locally
> of finite type, let `x ⤳ x'` be a specialization in `X` with `x'` closed in its own fibre
> `X_{f x'}`, and write `d = natTrdegFiber f x`. Then the remark holds — for *every* closed subset
> `W` of the fibre `X_{f x}` not containing `x` there is a chain
>
> `x = c 0 ⤳ c 1 ⤳ ⋯ ⤳ c d ⤳ x'`
>
> whose first `d` steps are immediate specializations inside `X_{f x}`, which avoids `W`, and whose
> last term `c d` is a closed point of `X_{f x}` — if and only if `x = x'` or `f x ≠ f x'`.
>
> The reverse implication is the assertion of the remark and carries its mathematical content: it
> is `AlgebraicGeometry.exists_chain_isImmediateSpecialization_specializes_fiber`, which runs the
> argument of the source.
>
> The forward implication settles the one remaining situation, a nontrivial specialization inside
> one fibre, where the remark fails. If `f x = f x'` then `x'` is a point `z` of `X_{f x}`, closed
> there, so `{z}` is a closed subset of `X_{f x}`; were `x ≠ x'` it would not contain `x`, hence
> would be a legitimate set to avoid, and the chain avoiding it would end in a point of `X_{f x}`,
> closed there, specializing to `x'` and different from `z`. But a point of a fibre closed in that
> fibre is the only point of the fibre it specializes to
> (`AlgebraicGeometry.eq_of_fiberι_specializes_of_isClosed`), so that last term is `z` after all.
> For `X = 𝔸¹` over a field, `x` its generic point and `x'` a closed point, every hypothesis of
> the remark holds and its conclusion is therefore false. This is the gap inherited from
> Stacks 053U, whose density conclusion supplies the point to walk down to and which is stated
> with the same range of validity in
> `AlgebraicGeometry.closure_closedPoints_between_fiber_eq_iff`; the source's own proof draws the
> same line, at the prime-avoidance step (see the module docstring).
>
> The closed set to be avoided is quantified inside the existence statement because that is where
> the source puts it: the points `x_i` can be chosen to avoid *any* closed subset of `X_s` not
> containing `x`. Fixing a single `W` instead would make the equivalence false, `W = ∅` being
> avoided by a chain in every configuration.

```lean
public theorem exists_chain_isImmediateSpecialization_specializes_fiber_iff
    (f : X ⟶ S) [LocallyOfFiniteType f] (x x' : X) (hxx' : x ⤳ x')
    (hx' : IsClosed ({f.asFiber x'} : Set (f.fiber (f x')))) :
    (∀ W : Set (f.fiber (f x)), IsClosed W → f.asFiber x ∉ W →
        ∃ c : Fin (natTrdegFiber f x + 1) → f.fiber (f x),
          c 0 = f.asFiber x ∧
          (∀ i : Fin (natTrdegFiber f x),
            IsImmediateSpecialization (c i.castSucc) (c i.succ)) ∧
          IsClosed ({c (Fin.last (natTrdegFiber f x))} : Set (f.fiber (f x))) ∧
          f.fiberι (f x) (c (Fin.last (natTrdegFiber f x))) ⤳ x' ∧
          ∀ i, c i ∉ W) ↔
      x = x' ∨ f x ≠ f x'
```

## Tag 05GT, a lemma

[Tag 05GT](https://stacks.math.columbia.edu/tag/05GT) in the Stacks Project.

**`Stacks.ClosedPointsFibre.exists_quotient_isLocalization_quasiFinite_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/LocalRing.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/LocalRing.lean#L55).

> An open of the spectrum of an essentially finite type local algebra which meets the
> complement of the closed fibre contains a prime whose quotient is a localization of a
> quasi-finite algebra.

```lean
theorem exists_quotient_isLocalization_quasiFinite_of_isOpen
    {A B : Type u} [CommRing A] [CommRing B] [IsLocalRing A] [IsLocalRing B]
    [IsNoetherianRing A]
    (f : A →+* B) (hf : IsLocalHom f)
    (heft : IsEssentiallyOfFiniteType A B f)
    (hres : letI : IsLocalHom f := hf;
      letI := (IsLocalRing.ResidueField.map f).toAlgebra;
      Module.Finite (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B))
    (V : Set (PrimeSpectrum B)) (hV : IsOpen V)
    (hne : ∃ q : PrimeSpectrum B,
      q ∈ V ∧ q.asIdeal.comap f ≠ IsLocalRing.maximalIdeal A) :
    ∃ q : PrimeSpectrum B, q ∈ V ∧
      q.asIdeal.comap f ≠ IsLocalRing.maximalIdeal A ∧
      letI := f.toAlgebra;
      ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C)
        (_ : Algebra.FiniteType A C) (_ : Algebra.QuasiFinite A C)
        (M : Submonoid C) (_ : Algebra C (B ⧸ q.asIdeal)),
        IsScalarTower A C (B ⧸ q.asIdeal) ∧ IsLocalization M (B ⧸ q.asIdeal)
```

## Tag 05GU, a lemma

[Tag 05GU](https://stacks.math.columbia.edu/tag/05GU) in the Stacks Project.

**`Stacks.ClosedPointsFibre.exists_closedSubscheme_quasiFiniteAt_meeting_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/ClosedSubscheme.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/ClosedSubscheme.lean#L70).

> Let `f : X ⟶ S` be locally of finite type with `S` locally Noetherian, and let `x` be closed
> in its fibre. If some point of the open `U` specializes to `x` and lies over a point other than
> `f x`, then there are a closed immersion `i : Z ⟶ X` and a point `xZ` of `Z` over `x` at which
> `i ≫ f` is quasi-finite, together with a generalization `zZ` of `xZ` mapping into `U` and lying
> over a point other than `f x`.

```lean
theorem exists_closedSubscheme_quasiFiniteAt_meeting_open
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (x : X) (U : X.Opens)
    (hx : IsClosed ({f.asFiber x} : Set (f.fiber (f x))))
    (hU : ∃ x' : X, x' ∈ U.1 ∧ x' ⤳ x ∧ f x' ≠ f x) :
    ∃ (Z : Scheme.{u}) (i : Z ⟶ X), IsClosedImmersion i ∧
      ∃ xZ : Z, i xZ = x ∧ quasiFiniteAt (i ≫ f) xZ ∧
        ∃ zZ : Z, i zZ ∈ U.1 ∧ zZ ⤳ xZ ∧ f (i zZ) ≠ f x
```

## Tag 05GV, a remark

[Tag 05GV](https://stacks.math.columbia.edu/tag/05GV) in the Stacks Project.

**`AlgebraicGeometry.closure_closedPoints_between_fiber_eq_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/DenseClosedPoints.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/DenseClosedPoints.lean#L231). The attribute's comment: “the theorem the remark asserts, by the route it sketches; the hypothesis `f x ≠ f x'` (or `x = x'`) is added, Stacks 053U being false without it”.

> **Stacks 053U for a locally Noetherian base.** For `f : X ⟶ S` locally of finite type with
> `S` locally Noetherian, `x ⤳ x'` with `x'` closed in its fibre and `f x ≠ f x'` (or `x = x'`),
> the points of `X_{f x}` closed in `X_{f x}` and lying between `x` and `x'` are dense in the
> closure of `x` in `X_{f x}`.

```lean
public theorem closure_closedPoints_between_fiber_eq_of_isLocallyNoetherian {X S : Scheme.{u}}
    (f : X ⟶ S) [LocallyOfFiniteType f] [IsLocallyNoetherian S] (x x' : X) (hxx' : x ⤳ x')
    (hx' : IsClosed ({f.asFiber x'} : Set (f.fiber (f x'))))
    (hs : f x ≠ f x' ∨ x = x') :
    closure {y : f.fiber (f x) | IsClosed ({y} : Set (f.fiber (f x))) ∧
        x ⤳ f.fiberι (f x) y ∧ f.fiberι (f x) y ⤳ x'} =
      closure ({f.asFiber x} : Set (f.fiber (f x)))
```

## Tag 05GW, a lemma

[Tag 05GW](https://stacks.math.columbia.edu/tag/05GW) in the Stacks Project.

**`Stacks.ClosedPointsFibre.exists_closedSubscheme_quasiFiniteAt_meeting_open_of_mem_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/ClosedSubscheme.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedPointsFibre/ClosedSubscheme.lean#L259).

> Let `f : X ⟶ S` be locally of finite type with `S` locally Noetherian, and let `x` be closed
> in its fibre. If `x` lies in the closure of an open `U` no point of which lies over `f x`, then
> there are a closed immersion `i : Z ⟶ X` and a point `xZ` of `Z` over `x` at which `i ≫ f` is
> quasi-finite, together with a generalization `zZ` of `xZ` mapping into `U` and lying over a point
> other than `f x`.

```lean
theorem exists_closedSubscheme_quasiFiniteAt_meeting_open_of_mem_closure
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (x : X) (U : X.Opens)
    (hx : IsClosed ({f.asFiber x} : Set (f.fiber (f x))))
    (hU : ∀ y : X, y ∈ U.1 → f y ≠ f x)
    (hclosure : x ∈ closure (U.1 : Set X)) :
    ∃ (Z : Scheme.{u}) (i : Z ⟶ X), IsClosedImmersion i ∧
      ∃ xZ : Z, i xZ = x ∧ quasiFiniteAt (i ≫ f) xZ ∧
        ∃ zZ : Z, i zZ ∈ U.1 ∧ zZ ⤳ xZ ∧ f (i zZ) ≠ f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.52, Tag 053Q](https://stacks.math.columbia.edu/tag/053Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
