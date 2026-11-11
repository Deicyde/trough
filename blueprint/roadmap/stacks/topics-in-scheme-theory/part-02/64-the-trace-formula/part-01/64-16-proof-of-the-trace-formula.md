---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.exists_compactification_and_traceFormulaUpToDim_one, Stacks.EtaleCohomology.compactSupportLefschetzNumber_eq_localLefschetzNumber, Stacks.EtaleCohomology.compactificationFieldBaseChange, Stacks.EtaleCohomology.geometricCompactSupportCohomology, Stacks.EtaleCohomology.geometricCompactSupportCohomologyGroup, Stacks.EtaleCohomology.geometricCompactSupportComparison, Stacks.EtaleCohomology.geometricCompactSupportGroupComparison, Stacks.EtaleCohomology.geometricCompactSupportCanonicalComparison
statement: formalized
proof: formalized
---

# 64.16 Proof of the trace formula

Section 64.16 of the Stacks Project, [Tag 03UF](https://stacks.math.columbia.edu/tag/03UF). 3 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03UG, a theorem

[Tag 03UG](https://stacks.math.columbia.edu/tag/03UG) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_compactification_and_traceFormulaUpToDim_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaCtf.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaCtf.lean#L78).

> **[Stacks, Tag 03UG]: the trace formula for curves.** Let `k` be a finite field with
> `#k = p ^ q`, `k̄` an algebraic closure of `k`, and `Λ` a finite ring whose cardinality is prime
> to that of `k`. Every separated scheme `X` of finite type over `k` of dimension at most one has a
> compactification over `k`, and for every compactification `j` of `X` and every
> `K ∈ D_ctf(X, Λ)`, `RΓ_c(X_k̄, K)` (computed through `j`) and the stalks `K_x̄` at the rational
> points are perfect and
>
> `Tr(π_X^* | RΓ_c(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)`
>
> in `Λ^♮`.

```lean
theorem exists_compactification_and_traceFormulaUpToDim_one (B : BigEtaleSite.{u}) (Λ : Type)
    [Ring Λ] [Finite Λ] {k : Type u} [Field k] [Fintype k] (kbar : Type u) [Field kbar]
    [IsAlgClosed kbar] [Algebra k kbar] [Algebra.IsAlgebraic k kbar] (p q : ℕ) [Fact p.Prime]
    [CharP k p] [CharP kbar p] (hcard : Fintype.card k = p ^ q)
    (hcop : Nat.Coprime (Nat.card Λ) (Fintype.card k)) :
    (∀ (X : B.Scheme) (f : X.obj ⟶ Spec (.of k)) [QuasiCompact f] [LocallyOfFiniteType f]
      [IsSeparated f], topologicalKrullDim X.obj ≤ ((1 : ℕ) : WithBot ℕ∞) →
      Nonempty (CompactificationOf (Over.mk f))) ∧
    TraceFormulaUpToDim B Λ kbar p q hcard 1
```

**`Stacks.EtaleCohomology.compactSupportLefschetzNumber_eq_localLefschetzNumber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaDimensionOne.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaDimensionOne.lean#L313). The attribute's comment: “RESTRICTED: 03UH with both sides built from the scheme; the extra hypotheses are 03TV as hperf and hstalkPerfect (K is a bounded below complex of étale sheaves of modules rather than an object of the D\_ctf of 03TQ: the two small étale sites are identified by SmallEtale.sheafEquiv, but the transport of finite Tor dimension across it and the direction (1) => (2) of 03TT are missing), finiteness of X(k), the Step 1 dévissage with the identification of its pieces (devissage, hglobal, hstalk), and the Steps 7 to 9 Galois decomposition feeding 03TZ (hdecomposition, hdivisible, hannihilate, hlevel); Steps 3 to 6 are not formalized”.

> **The trace formula in dimension at most one (Stacks 03UG).**  Let `k` be a finite field
> with `p ^ q` elements, let `k̄` be an algebraically closed extension of `k`, let `X` be a
> separated scheme of finite type over `k` of dimension at most one, let `Λ` be a finite ring
> whose cardinality is prime to that of `k`, and let `K` be a bounded below complex of sheaves of
> `Λ`-modules on the small étale site of `X`.  Then
>
> `Tr(π_X^* | RΓ_c(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)`
>
> in `Λ^natural`, the left hand side being the trace of the action induced on
> `RΓ_c(X_k̄, K|_{X_k̄})` by an extension of the geometric Frobenius `π_X × id` of
> [Stacks, Tag 03SQ] to a compactification of `X_k̄` over `Spec k̄`, and the right hand side the
> sum over the rational points of the traces of the geometric Frobenius of [Stacks, Tag 03SW] on
> the stalks of `K` at the geometric points above them.
>
> Perfectness of `RΓ_c(X_k̄, K|_{X_k̄})` and of each stalk, finiteness of `X(k)`, the dévissage of
> Step 1 of the source with the identification of its graded pieces, and the Galois decomposition
> of Steps 7 to 9 are hypotheses; the implementation notes of this file record what each of them
> is and what remains unformalized.

```lean
public theorem compactSupportLefschetzNumber_eq_localLefschetzNumber
    {k : Type u} [Field k] [Fintype k] {p q : ℕ} [Fact p.Prime] [CharP k p]
    (hcard : Fintype.card k = p ^ q) (Y : Over (Spec (.of k)))
    [IsSeparated Y.hom] [LocallyOfFiniteType Y.hom] [QuasiCompact Y.hom]
    (_hdim : topologicalKrullDim Y.left ≤ 1)
    (kbar : Type u) [Field kbar] [IsAlgClosed kbar] [Algebra k kbar] [CharP kbar p]
    (Λ : Type r) [Ring Λ] [Finite Λ]
    (_hcoprime : Nat.Coprime (Nat.card Λ) (Fintype.card k))
    (K : CochainComplex.Plus (EtaleModules.{u, r} Λ Y.left))
    [Fintype (rationalPoints Y.hom)]
    (j : CompactificationOf
      (Over.mk (pullback.snd Y.hom (Stacks.Frobenius.specAlgebraMap k kbar))))
    (E : CompactificationEndomorphism j
      (Stacks.Frobenius.geometricFrobeniusBaseChange Y kbar p q hcard))
    (γ : 𝟭 (DerivedCategory.Plus (EtaleModules.{u, r} Λ j.space)) ⟶
      etaleModuleDerivedDirectImage.{u, r} Λ E.hom)
    (hperf : StacksDraft.Perfect.IsPerfect (DerivedCategory.Plus.ι.obj
      ((compactlySupportedCohomology.{u, r} kbar
          (pullback.snd Y.hom (Stacks.Frobenius.specAlgebraMap k kbar)) j Λ).obj
        (baseChangeCoefficients.{u, r} Λ Y kbar K))))
    (hstalkPerfect : ∀ x : rationalPoints Y.hom, StacksDraft.Perfect.IsPerfect
      (DerivedCategory.Q.obj (rationalPointStalkComplex.{u, r} Λ kbar x.1 K)))
    (devissage : LefschetzDevissage.{r, max (u + 1) r, u} Λ (rationalPoints Y.hom))
    (hglobal : devissage.globalDatum =
      frobeniusActionOnCompactSupport.{u, r} Λ E γ
        (baseChangeCoefficients.{u, r} Λ Y kbar K) hperf)
    (hstalk : devissage.stalkDatum =
      geometricFrobeniusStalkDatum.{u, r} Λ kbar p q hcard Y.hom K hstalkPerfect)
    (group : Type t) [Fintype group] (prime exponent level : ℕ)
    (stabilizerExponent : group → ℕ) (coefficientTrace : group → ℤ)
    (moduleTrace : group → AdditiveCommutatorQuotient Λ)
    (hprime : Nat.Prime prime)
    (hannihilate : ∀ y : AdditiveCommutatorQuotient Λ, ((prime : ℤ) ^ exponent) • y = 0)
    (hlevel : ∀ g : group, stabilizerExponent g + exponent ≤ level)
    (hdecomposition : globalLefschetzNumber Λ devissage.openDatum =
      ∑ g : group, coefficientTrace g • moduleTrace g)
    (hdivisible : ∀ g : group, ((prime : ℤ) ^ level) ∣
      ((prime : ℤ) ^ stabilizerExponent g) * coefficientTrace g) :
    compactSupportLefschetzNumber.{u, r} Λ E γ
        (baseChangeCoefficients.{u, r} Λ Y kbar K) hperf =
      localLefschetzNumber Λ (rationalPoints Y.hom)
        (geometricFrobeniusStalkDatum.{u, r} Λ kbar p q hcard Y.hom K hstalkPerfect)
```

## Tag 03UI, a remark

[Tag 03UI](https://stacks.math.columbia.edu/tag/03UI) in the Stacks Project.

**`Stacks.EtaleCohomology.compactificationFieldBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean#L133). The attribute's comment: “item (2): the base change X̄\_k̄ of a compactification X̄ of X over k is a compactification of X\_k̄ over k̄, which is where RΓ\_c(X\_k̄, -) is formed”.

> **The base change `X̄_k̄` of a compactification of `X` over `k`**, as a compactification of
> `X_k̄` over `k̄`: the fibre product `X̄ ×_{Spec k} Spec k̄` is proper over `Spec k̄` because `X̄`
> is proper over `Spec k`, and `X_k̄ ⟶ X̄_k̄` is an open immersion because `X ⟶ X̄` is one.  This
> is the ambient scheme the source takes `RΓ_c(X_k̄, -)` on.

```lean
public def compactificationFieldBaseChange :
    CompactificationOf (Over.mk (pullback.snd f (Stacks.Frobenius.specAlgebraMap k kbar)))
```

**`Stacks.EtaleCohomology.geometricCompactSupportCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean#L159). The attribute's comment: “item (2): RΓ\_c(X\_k̄, K) := RΓ(X̄\_k̄, j\_! K) for a chosen compactification j of X over k, taken through its base change”.

> **The complex `RΓ_c(X_k̄, K) = RΓ(X̄_k̄, j_! K)`** of the source: cohomology with compact
> support of a bounded below complex of sheaves of `Λ`-modules on the small étale site of the
> base change `X_k̄`, formed through the base change `X̄_k̄` of a compactification `X̄` of `X`
> over `k`.  The compactification is an argument, not a choice.

```lean
public abbrev geometricCompactSupportCohomology :
    DerivedCategory.Plus
        (EtaleModules.{u, r} Λ (pullback f (Stacks.Frobenius.specAlgebraMap k kbar))) ⥤
      DerivedCategory.Plus (ModuleCat.{max (u + 1) r} Λ)
```

**`Stacks.EtaleCohomology.geometricCompactSupportCohomologyGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean#L169). The attribute's comment: “item (2): H^i\_c(X\_k̄, K) is the i-th cohomology of RΓ\_c(X\_k̄, K)”.

> **The module `H^i_c(X_k̄, K)`**: the `i`-th cohomology of `RΓ_c(X_k̄, K)`.

```lean
public abbrev geometricCompactSupportCohomologyGroup (i : ℤ) :
    DerivedCategory.Plus
        (EtaleModules.{u, r} Λ (pullback f (Stacks.Frobenius.specAlgebraMap k kbar))) ⥤
      ModuleCat.{max (u + 1) r} Λ
```

**`Stacks.EtaleCohomology.geometricCompactSupportComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean#L201). The attribute's comment: “item (2): RΓ\_c(X\_k̄, -) is independent of the compactification, reduced to the independence of Rf\_! of 0F7I, which is a hypothesis here”.

> **Independence of the compactification.**  An isomorphism of the derived lower shriek
> functors attached to two compactifications of `X` over `k`, which is [Stacks, Tag 0F7I],
> induces an isomorphism of the complexes `RΓ_c(X_k̄, -)` they present, natural in the
> coefficient complex.

```lean
public def geometricCompactSupportComparison
    (e : geometricLowerShriek.{u, r} f j₁ kbar Λ ≅ geometricLowerShriek.{u, r} f j₂ kbar Λ) :
    geometricCompactSupportCohomology.{u, r} f j₁ kbar Λ ≅
      geometricCompactSupportCohomology.{u, r} f j₂ kbar Λ
```

**`Stacks.EtaleCohomology.geometricCompactSupportGroupComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCompactification.lean#L233). The attribute's comment: “item (2): H^i\_c(X\_k̄, -) is independent of the compactification, induced by the comparison of the complexes”.

> **Independence of the compactification for `H^i_c`.**  The comparison of the complexes
> induces an isomorphism of the modules `H^i_c(X_k̄, -)` in every degree, natural in the
> coefficient complex.

```lean
public def geometricCompactSupportGroupComparison
    (e : geometricLowerShriek.{u, r} f j₁ kbar Λ ≅ geometricLowerShriek.{u, r} f j₂ kbar Λ)
    (i : ℤ) :
    geometricCompactSupportCohomologyGroup.{u, r} f j₁ kbar Λ i ≅
      geometricCompactSupportCohomologyGroup.{u, r} f j₂ kbar Λ i
```

**`Stacks.EtaleCohomology.geometricCompactSupportCanonicalComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricCompactSupportCanonicalComparison.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricCompactSupportCanonicalComparison.lean#L217). The attribute's comment: “(2): independence of the compactification -- RΓ\_c(X\_k̄, -) = RΓ(X̄\_k̄, j\_! -) does not depend on the compactification X̄ of X over k of dimension at most one (proper, which a projective X̄ is): canonical isomorphism through the closure of X in X̄₁ ×\_k X̄₂”.

> **Remark 03UI (2): `RΓ_c(X_k̄, -)` is independent of the compactification.**  Let `k` be a
> field, `X` a separated scheme of finite type over `k`, `k̄` an extension field of `k` and `Λ` a
> ring.  For any two compactifications `X ⟶ X̄₁` and `X ⟶ X̄₂` of `X` over `k` (open immersions
> into proper `k`-schemes, which projective ones are) of dimension at most one, the complexes
> `RΓ(X̄₁_k̄, j₁! K)` and `RΓ(X̄₂_k̄, j₂! K)` are canonically isomorphic, naturally in the bounded
> below complex `K` of sheaves of `Λ`-modules on `X_k̄`.  The isomorphism is induced by the
> canonical isomorphism `geometricLowerShriekCanonicalIso` of the derived lower shriek functors,
> through the closure of `X` in `X̄₁ ×_k X̄₂`.
>
> The coefficient ring is taken in `Type` (universe `0`), as in the companion results of
> Tags 03VK and 03VL: integral base change for sheaves of modules, through which the finite
> projections of the dominating compactification are handled, is available at that universe. A
> finite ring, the coefficient ring of the source, is isomorphic to one in `Type`.

```lean
def geometricCompactSupportCanonicalComparison :
    geometricCompactSupportCohomology.{u, 0} f c₁ kbar Λ ≅
      geometricCompactSupportCohomology.{u, 0} f c₂ kbar Λ
```

**`Stacks.EtaleCohomology.geometricCompactSupportGroupCanonicalComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricCompactSupportCanonicalComparison.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricCompactSupportCanonicalComparison.lean#L229). The attribute's comment: “(2): independence of the compactification -- H^i\_c(X\_k̄, -) does not depend on the compactification X̄ of X over k of dimension at most one, in every degree”.

> **Remark 03UI (2): `H^i_c(X_k̄, -)` is independent of the compactification**, in every degree,
> naturally in the coefficient complex: the isomorphism induced on cohomology by
> `geometricCompactSupportCanonicalComparison`.  The coefficient ring is taken in `Type`, as in
> `geometricCompactSupportCanonicalComparison`.

```lean
def geometricCompactSupportGroupCanonicalComparison (i : ℤ) :
    geometricCompactSupportCohomologyGroup.{u, 0} f c₁ kbar Λ i ≅
      geometricCompactSupportCohomologyGroup.{u, 0} f c₂ kbar Λ i
```

**`Stacks.EtaleCohomology.compactSupportLefschetzNumber_eq_localLefschetzNumber_of_galoisDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaAnyDimension.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaAnyDimension.lean#L84). The attribute's comment: “item (1) RESTRICTED: the 03UG identity with no bound on the dimension of X, from the Step 1 devissage with its identifications (devissage, hglobal, hstalk) and the Steps 7 to 9 Galois descent of 03TZ; the source's reduction of the general case to dimension one is not here”.

> **The trace formula in any dimension (Stacks 03UI, item (1)).**  Let `k` be a finite field
> with `p ^ q` elements, let `k̄` be an algebraically closed extension of `k`, let `X` be a
> separated scheme of finite type over `k` — of arbitrary dimension — let `Λ` be a finite ring
> whose cardinality is prime to that of `k`, and let `K` be a bounded below complex of sheaves of
> `Λ`-modules on the small étale site of `X`.  Then
>
> `Tr(π_X^* | RΓ_c(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)`
>
> in `Λ^natural`, given the dévissage of `RΓ_c(X_k̄, K)` along the rational points with the
> identification of its graded pieces and the Galois descent of Steps 7 to 9 of the source.  The
> bound `topologicalKrullDim X ≤ 1` of
> `Stacks.EtaleCohomology.compactSupportLefschetzNumber_eq_localLefschetzNumber` plays no part in
> the deduction and is absent here.

```lean
public theorem compactSupportLefschetzNumber_eq_localLefschetzNumber_of_galoisDescent
    {k : Type u} [Field k] [Fintype k] {p q : ℕ} [Fact p.Prime] [CharP k p]
    (hcard : Fintype.card k = p ^ q) (Y : Over (Spec (.of k)))
    [IsSeparated Y.hom] [LocallyOfFiniteType Y.hom] [QuasiCompact Y.hom]
    (kbar : Type u) [Field kbar] [IsAlgClosed kbar] [Algebra k kbar] [CharP kbar p]
    (Λ : Type r) [Ring Λ] [Finite Λ]
    (_hcoprime : Nat.Coprime (Nat.card Λ) (Fintype.card k))
    (K : CochainComplex.Plus (EtaleModules.{u, r} Λ Y.left))
    [Fintype (rationalPoints Y.hom)]
    (j : CompactificationOf
      (Over.mk (pullback.snd Y.hom (Stacks.Frobenius.specAlgebraMap k kbar))))
    (E : CompactificationEndomorphism j
      (Stacks.Frobenius.geometricFrobeniusBaseChange Y kbar p q hcard))
    (γ : 𝟭 (DerivedCategory.Plus (EtaleModules.{u, r} Λ j.space)) ⟶
      etaleModuleDerivedDirectImage.{u, r} Λ E.hom)
    (hperf : StacksDraft.Perfect.IsPerfect (DerivedCategory.Plus.ι.obj
      ((compactlySupportedCohomology.{u, r} kbar
          (pullback.snd Y.hom (Stacks.Frobenius.specAlgebraMap k kbar)) j Λ).obj
        (baseChangeCoefficients.{u, r} Λ Y kbar K))))
    (hstalkPerfect : ∀ x : rationalPoints Y.hom, StacksDraft.Perfect.IsPerfect
      (DerivedCategory.Q.obj (rationalPointStalkComplex.{u, r} Λ kbar x.1 K)))
    (devissage : LefschetzDevissage.{r, max (u + 1) r, u} Λ (rationalPoints Y.hom))
    (hglobal : devissage.globalDatum =
      frobeniusActionOnCompactSupport.{u, r} Λ E γ
        (baseChangeCoefficients.{u, r} Λ Y kbar K) hperf)
    (hstalk : devissage.stalkDatum =
      geometricFrobeniusStalkDatum.{u, r} Λ kbar p q hcard Y.hom K hstalkPerfect)
    (group : Type t) [Fintype group]
    (descent : LefschetzGaloisDescent.{r, max (u + 1) r, u, t} Λ devissage group) :
    compactSupportLefschetzNumber.{u, r} Λ E γ
        (baseChangeCoefficients.{u, r} Λ Y kbar K) hperf =
      localLefschetzNumber Λ (rationalPoints Y.hom)
        (geometricFrobeniusStalkDatum.{u, r} Λ kbar p q hcard Y.hom K hstalkPerfect)
```

**`Stacks.EtaleCohomology.canonicalTraceFormula_of_isCtf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaAnyDimensionCtf.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaAnyDimensionCtf.lean#L52). The attribute's comment: “(1): the trace formula in any dimension: Tag 03UG for `X` separated of finite type over `k` with no bound on its dimension, through every compactification. `Λ : Type` (universe 0), see the module docstring.”.

> **The trace formula in any dimension ([Stacks, Tag 03UI] (1)).** Let `k` be a finite field
> with `p ^ q` elements and `k̄` an algebraic closure, `X` a separated scheme of finite type over `k`
> of any dimension, `Λ` a finite ring whose cardinality is prime to that of `k`, and
> `K ∈ D_ctf(X, Λ)`. Then for every compactification `j : X ⟶ X̄` over `k`, the complex
> `RΓ_c(X_k̄, K) = RΓ(X̄_k̄, (j_! K)|_{X̄_k̄})` and the stalks `K_x̄` at the rational points are
> perfect, and `Tr(π_X^* | RΓ_c(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)` in `Λ^natural`, for the
> canonical Frobenius actions (`Stacks.EtaleCohomology.CanonicalTraceFormula`). The coefficient
> ring is in `Type` (see the module docstring).

```lean
theorem canonicalTraceFormula_of_isCtf (B : BigEtaleSite.{u}) (Λ : Type) [Ring Λ] [Finite Λ]
    {k : Type u} [Field k] [Fintype k] (kbar : Type u) [Field kbar] [IsAlgClosed kbar]
    [Algebra k kbar] [Algebra.IsAlgebraic k kbar] (p q : ℕ) [Fact p.Prime] [CharP k p]
    [CharP kbar p] (hcard : Fintype.card k = p ^ q)
    (hcop : Nat.Coprime (Nat.card Λ) (Fintype.card k))
    (X : B.Scheme) (f : X.obj ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] (K : CochainComplex.Plus (EtaleModules.{u, 0} Λ X.obj))
    (hK : IsCtf B X Λ (DerivedCategory.Q.obj K.obj)) (j : CompactificationOf (Over.mk f)) :
    CanonicalTraceFormula Λ kbar p q hcard f j K
```

## Tag 03UJ, a remark

[Tag 03UJ](https://stacks.math.columbia.edu/tag/03UJ) in the Stacks Project.

**`Stacks.EtaleCohomology.localLefschetzNumber_constantStalkDatum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantCoefficientTraceFormula.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantCoefficientTraceFormula.lean#L102). The attribute's comment: “with constant coefficients the right hand side of 03UG collapses to #X(k) times the trace at one rational point, which is the point count Weil's formula 03U1 computes”.

> **With constant coefficients the local Lefschetz number is a point count.**  The sum
> `∑_{x ∈ X(k)} Tr(π_x | K_x̄)` of [Stacks, Tag 03TY] has equal terms when the coefficient system
> is constant, so it is `#X(k)` times the trace at a single rational point.

```lean
public theorem localLefschetzNumber_constantStalkDatum (Λ : Type u) [Ring Λ] [Finite Λ]
    (points : Type w) [Fintype points] (S : PerfectDerivedCategory.{u, r} Λ)
    (g : S.obj ⟶ S.obj) :
    localLefschetzNumber Λ points (constantStalkDatum.{u, r, w} Λ points S g) =
      (Fintype.card points : ℤ) • perfectDerivedTrace Λ S g
```

**`Stacks.EtaleCohomology.compactSupportLefschetzNumber_eq_weil_of_constantCoefficients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantCoefficientTraceFormula.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ConstantCoefficientTraceFormula.lean#L126). The attribute's comment: “RESTRICTED: 03UG specialised to constant coefficients computes #X(k), and 03U1 evaluates that count as 1 - Tr\_J + deg; the hypotheses of the library's 03UG are carried unchanged, and the constancy of the stalks and the fixed point count are hypotheses”.

> **The trace formula with constant coefficients is Weil's formula (Stacks 03UJ).**  In the
> situation of `Stacks.EtaleCohomology.compactSupportLefschetzNumber_eq_localLefschetzNumber`,
> suppose the coefficient system is constant, so that the stalk of `K` at every rational point is
> one perfect complex `S` with one endomorphism `g` on it, and suppose the number of rational
> points of `X` is the intersection number `V(π_X) = Δ_C · Γ_{π_X}` of Weil's formula for the
> geometric Frobenius.  Then
>
> `Tr(π_X^* | RΓ_c(X_k̄, K)) = (1 - Tr_J(π_X^*) + deg π_X) · Tr(π_x | K_x̄)`
>
> in `Λ^natural`: the right hand side of the trace formula is the point count, and Weil's formula
> [Stacks, Tag 03U1] evaluates it on the jacobian of the curve.

```lean
public theorem compactSupportLefschetzNumber_eq_weil_of_constantCoefficients
    {k : Type u} [Field k] [Fintype k] {p q : ℕ} [Fact p.Prime] [CharP k p]
    (hcard : Fintype.card k = p ^ q) (Y : Over (Spec (.of k)))
    [IsSeparated Y.hom] [LocallyOfFiniteType Y.hom] [QuasiCompact Y.hom]
    (hdim : topologicalKrullDim Y.left ≤ 1)
    (kbar : Type u) [Field kbar] [IsAlgClosed kbar] [Algebra k kbar] [CharP kbar p]
    (Λ : Type r) [Ring Λ] [Finite Λ]
    (hcoprime : Nat.Coprime (Nat.card Λ) (Fintype.card k))
    (K : CochainComplex.Plus (EtaleModules.{u, r} Λ Y.left))
    [Fintype (rationalPoints Y.hom)]
    (j : CompactificationOf
      (Over.mk (pullback.snd Y.hom (Stacks.Frobenius.specAlgebraMap k kbar))))
    (E : CompactificationEndomorphism j
      (Stacks.Frobenius.geometricFrobeniusBaseChange Y kbar p q hcard))
    (γ : 𝟭 (DerivedCategory.Plus (EtaleModules.{u, r} Λ j.space)) ⟶
      etaleModuleDerivedDirectImage.{u, r} Λ E.hom)
    (hperf : StacksDraft.Perfect.IsPerfect (DerivedCategory.Plus.ι.obj
      ((compactlySupportedCohomology.{u, r} kbar
          (pullback.snd Y.hom (Stacks.Frobenius.specAlgebraMap k kbar)) j Λ).obj
        (baseChangeCoefficients.{u, r} Λ Y kbar K))))
    (hstalkPerfect : ∀ x : rationalPoints Y.hom, StacksDraft.Perfect.IsPerfect
      (DerivedCategory.Q.obj (rationalPointStalkComplex.{u, r} Λ kbar x.1 K)))
    (devissage : LefschetzDevissage.{r, max (u + 1) r, u} Λ (rationalPoints Y.hom))
    (hglobal : devissage.globalDatum =
      frobeniusActionOnCompactSupport.{u, r} Λ E γ
        (baseChangeCoefficients.{u, r} Λ Y kbar K) hperf)
    (hstalk : devissage.stalkDatum =
      geometricFrobeniusStalkDatum.{u, r} Λ kbar p q hcard Y.hom K hstalkPerfect)
    (group : Type t) [Fintype group] (prime exponent level : ℕ)
    (stabilizerExponent : group → ℕ) (coefficientTrace : group → ℤ)
    (moduleTrace : group → AdditiveCommutatorQuotient Λ)
    (hprime : Nat.Prime prime)
    (hannihilate : ∀ y : AdditiveCommutatorQuotient Λ, ((prime : ℤ) ^ exponent) • y = 0)
    (hlevel : ∀ g : group, stabilizerExponent g + exponent ≤ level)
    (hdecomposition : globalLefschetzNumber Λ devissage.openDatum =
      ∑ g : group, coefficientTrace g • moduleTrace g)
    (hdivisible : ∀ g : group, ((prime : ℤ) ^ level) ∣
      ((prime : ℤ) ^ stabilizerExponent g) * coefficientTrace g)
    (S : PerfectDerivedCategory.{r, max (u + 1) r} Λ) (g : S.obj ⟶ S.obj)
    (hconstant : geometricFrobeniusStalkDatum.{u, r} Λ kbar p q hcard Y.hom K hstalkPerfect =
      constantStalkDatum.{r, max (u + 1) r, u} Λ (rationalPoints Y.hom) S g)
    {Adiv : Type w} [AddCommGroup Adiv] {EndJ : Type z} [Ring EndJ]
    (W : JacobianCorrespondence Adiv EndJ) (frobenius : W.EndomorphismData)
    (hfixedPoints : (Fintype.card (rationalPoints Y.hom) : ℤ) =
      W.fixedPointNumber frobenius) :
    compactSupportLefschetzNumber.{u, r} Λ E γ
        (baseChangeCoefficients.{u, r} Λ Y kbar K) hperf =
      (1 - W.trace frobenius.pullback + frobenius.degree) • perfectDerivedTrace Λ S g
```

**`Stacks.EtaleCohomology.traceFormula_constantCoefficients_eq_weil`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilComparisonTraceFormula.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilComparisonTraceFormula.lean#L74). References: SGA 4½ Rapport (3.2), “special case”.

> **[Stacks, Tag 03UJ]: the trace formula with constant coefficients recovers Weil's
> formula.** Let `X` be a smooth projective curve over a finite field `k` with `#k = p ^ q`, which
> stays a curve over an algebraic closure `k̄` (the setting of Weil's formula, Tag 03U1, on `X_k̄`),
> and let `ℓ ≠ p` be a prime. Let `π̄ = π_X × id` be the geometric Frobenius of `X_k̄`. Then
>
> * the trace formula (Tag 03UG) for `Λ = ℤ/ℓⁿ` gives `Tr(π_X^* | RΓ(X_k̄, ℤ/ℓⁿ)) = #X(k)`;
> * this Lefschetz number is `∑ᵢ (-1)ⁱ Tr(π̄^* | Hⁱ(X_k̄, ℤ/ℓⁿ))`;
> * the intersection number `V(π̄) = (Δ · Γ_π̄)` is `#X(k)` (the fixed points of `π̄` are simple);
> * hence Weil's formula (Tag 03U1) for `π̄` reads `#X(k) = 1 - Tr(π̄ | T_ℓ J) + deg π̄` in `ℤ_ℓ`.
>
> So both formulas count the same number `#X(k)`.

```lean
theorem traceFormula_constantCoefficients_eq_weil
    [IsCurve kbar (pullback.snd f (specAlgebraMap k kbar))] (hℓ : ℓ ≠ p) :
    canonicalCompactSupportLefschetzNumber.{u, 0} (ZMod (ℓ ^ n)) f (CompactificationOf.ofProper f)
        kbar p q hcard (constantCoefficients (ZMod (ℓ ^ n)) X.obj)
        (isPerfect_compactSupportFrobeniusCohomology_constantCoefficients B (ZMod (ℓ ^ n)) f
          (isProjective_of_isProper_of_isCurve f) kbar) =
      (Nat.card (rationalPoints f) : ℤ) • additiveCommutatorQuotientMk (ZMod (ℓ ^ n)) 1 ∧
    canonicalCompactSupportLefschetzNumber.{u, 0} (ZMod (ℓ ^ n)) f (CompactificationOf.ofProper f)
        kbar p q hcard (constantCoefficients (ZMod (ℓ ^ n)) X.obj)
        (isPerfect_compactSupportFrobeniusCohomology_constantCoefficients B (ZMod (ℓ ^ n)) f
          (isProjective_of_isProper_of_isCurve f) kbar) =
      additiveCommutatorQuotientMk (ZMod (ℓ ^ n))
        (∑ i ∈ Finset.range 3, (-1 : ZMod (ℓ ^ n)) ^ i * LinearMap.trace (ZMod (ℓ ^ n)) _
          ((etaleConstantCohomologyPullback
            (geometricFrobeniusBaseChange (Over.mk f) kbar p q hcard)
            (ZMod (ℓ ^ n)) i).toZModLinearMap (ℓ ^ n))) ∧
    AlgebraicGeometry.CurveGraph.fixedPointIntersection (pullback.snd f (specAlgebraMap k kbar))
        (IsCurve.topologicalKrullDim_eq_one (k := kbar)
          (f := pullback.snd f (specAlgebraMap k kbar))).le
        (geometricFrobeniusBaseChange (Over.mk f) kbar p q hcard)
          (geometricFrobeniusBaseChange_comp_toBase (Over.mk f) kbar p q hcard) =
      Nat.card (rationalPoints f) ∧
    (((Nat.card (rationalPoints f) : ℤ)) : ℤ_[ℓ]) =
      1 - AlgebraicGeometry.CurveGraph.jacobianTateTrace (pullback.snd f (specAlgebraMap k kbar))
        (IsCurve.topologicalKrullDim_eq_one (k := kbar)
          (f := pullback.snd f (specAlgebraMap k kbar))).le
        (geometricFrobeniusBaseChange (Over.mk f) kbar p q hcard)
          (geometricFrobeniusBaseChange_comp_toBase (Over.mk f) kbar p q hcard) ℓ +
        (AlgebraicGeometry.CurveGraph.curveMapDegree (pullback.snd f (specAlgebraMap k kbar))
          (geometricFrobeniusBaseChange (Over.mk f) kbar p q hcard)
          (geometricFrobeniusBaseChange_comp_toBase (Over.mk f) kbar p q hcard) : ℤ_[ℓ])
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.16, Tag 03UF](https://stacks.math.columbia.edu/tag/03UF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
