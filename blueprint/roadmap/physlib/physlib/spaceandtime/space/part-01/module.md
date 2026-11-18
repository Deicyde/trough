---
declaration: module
origin: cited
lean: Space.add_val, Space.add_apply, Space.nsmul_val, Space.nsmul_apply, Space.eq_vadd_zero, Space.add_vadd_zero, Space.smul_val, Space.smul_apply
statement: formalized
proof: formalized
---

# The structure of a module on Space

The module `Physlib.SpaceAndTime.Space.Module`, [Physlib/SpaceAndTime/Space/Module.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean): 96 declarations (15 instances with no name), 11 with a docstring.

> The scope of this module is to define on `Space d` the structure of a `Module`
> (aka vector space), a `Norm` and an `InnerProductSpace`, and give properties of these structures.
>
> These instances require certain non-canonical choices to be made, for example the choice
> of a zero and for a basis, a choice of orientation.

## Instances in Lean

> In Lean, an `instance` supplies a typeclass automatically. When a definition or
> theorem needs a structure such as `AddCommGroup (Space d)`, `Module ℝ (Space d)`,
> `NormedAddCommGroup (Space d)`, `InnerProductSpace ℝ (Space d)`, or
> `MeasurableSpace (Space d)`, typeclass inference searches for the corresponding
> instance and inserts it without the user passing it explicitly.
>
> These instances make `Space d` usable with standard mathematical notation and
> with the Mathlib API. For example, they allow expressions such as `p + q`,
> `c • p`, `‖p‖`, `inner ℝ p q`, and measurable-set arguments involving the Borel
> structure. They also make general theorems about modules, normed groups, inner
> product spaces, and measurable spaces apply directly to `Space d`.
>
> For `Space d`, these instances are intentional choices rather than inherited
> facts: the type was defined as a structure instead of an abbreviation for
> Euclidean space. In particular, the additive and module structures choose an
> origin, while the norm, inner product, and Borel structure choose the standard
> Euclidean coordinate geometry.

## A.1. Instance of an additive commutative monoid

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L54).

```lean
instance {d} : Add (Space d)
```

**`Space.add_val`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L58).

```lean
lemma add_val {d: ℕ} (x y : Space d) :
    (x + y).val = x.val + y.val
```

**`Space.add_apply`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L62).

```lean
lemma add_apply {d : ℕ} (x y : Space d) (i : Fin d) :
    (x + y) i = x i + y i
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L66).

```lean
instance {d} : AddCommMonoid (Space d)
```

**`Space.nsmul_val`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L86).

```lean
lemma nsmul_val {d : ℕ} (n : ℕ) (a : Space d) :
    (n • a).val = fun i => n • a.val i
```

**`Space.nsmul_apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L90).

```lean
lemma nsmul_apply {d : ℕ} (n : ℕ) (a : Space d) (i : Fin d) :
    (n • a) i = n • (a i)
```

**`Space.eq_vadd_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L93).

```lean
lemma eq_vadd_zero {d} (s : Space d) :
    ∃ v : EuclideanSpace ℝ (Fin d), s = v +ᵥ (0 : Space d)
```

**`Space.add_vadd_zero`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L99).

```lean
lemma add_vadd_zero {d} (v1 v2 : EuclideanSpace ℝ (Fin d)) :
    (v1 +ᵥ (0 : Space d)) + (v2 +ᵥ (0 : Space d)) = (v1 + v2) +ᵥ (0 : Space d)
```

## A.2. Instance of a module over `ℝ`

**An instance with no name**, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L110).

```lean
instance {d} : SMul ℝ (Space d)
```

**`Space.smul_val`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L114).

```lean
lemma smul_val {d : ℕ} (c : ℝ) (p : Space d) :
    (c • p).val = fun i => c * p.val i
```

**`Space.smul_apply`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L118).

```lean
lemma smul_apply {d : ℕ} (c : ℝ) (p : Space d) (i : Fin d) :
    (c • p) i = c * (p i)
```

**`Space.smul_vadd_zero`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L122).

```lean
lemma smul_vadd_zero {d} (k : ℝ) (v : EuclideanSpace ℝ (Fin d)) :
    k • (v +ᵥ (0 : Space d)) = (k • v) +ᵥ (0 : Space d)
```

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L127).

```lean
instance {d} : Module ℝ (Space d)
```

## A.3. Instance of an inner product space

**An instance with no name**, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L153).

```lean
noncomputable instance {d} : Norm (Space d)
```

**`Space.norm_eq`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L156).

```lean
lemma norm_eq {d} (p : Space d) : ‖p‖ = √ (∑ i, (p i) ^ 2)
```

**`Space.abs_eval_le_norm`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L160).

```lean
lemma abs_eval_le_norm {d} (p : Space d) (i : Fin d) :
    |p i| ≤ ‖p‖
```

**`Space.norm_sq_eq`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L166).

```lean
lemma norm_sq_eq {d} (p : Space d) :
    ‖p‖ ^ 2 = ∑ i, (p i) ^ 2
```

**`Space.point_dim_zero_eq`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L171).

```lean
lemma point_dim_zero_eq (p : Space 0) : p = 0
```

**`Space.norm_vadd_zero`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L175).

```lean
lemma norm_vadd_zero {d} (v : EuclideanSpace ℝ (Fin d)) :
    ‖v +ᵥ (0 : Space d)‖ = ‖v‖
```

**An instance with no name**, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L179).

```lean
instance : Neg (Space d)
```

**`Space.neg_val`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L183).

```lean
lemma neg_val {d : ℕ} (p : Space d) :
    (-p).val = fun i => - (p.val i)
```

**`Space.neg_apply`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L187).

```lean
lemma neg_apply {d : ℕ} (p : Space d) (i : Fin d) :
    (-p) i = - (p i)
```

**An instance with no name**, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L190).

```lean
noncomputable instance {d} : AddCommGroup (Space d)
```

**`Space.sub_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L197).

```lean
lemma sub_apply {d} (p q : Space d) (i : Fin d) :
    (p - q) i = p i - q i
```

**`Space.sub_val`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L202).

```lean
lemma sub_val {d} (p q : Space d) :
    (p - q).val = fun i => p.val i - q.val i
```

**`Space.vadd_zero_sub_vadd_zero`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L206).

```lean
lemma vadd_zero_sub_vadd_zero {d} (v1 v2 : EuclideanSpace ℝ (Fin d)) :
    (v1 +ᵥ (0 : Space d)) - (v2 +ᵥ (0 : Space d)) = (v1 - v2) +ᵥ (0 : Space d)
```

**`Space.dist_eq_norm`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L212).

```lean
lemma dist_eq_norm {d} (p q : Space d) :
    dist p q = ‖p - q‖
```

**An instance with no name**, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L215).

```lean
noncomputable instance {d} : SeminormedAddCommGroup (Space d)
```

**An instance with no name**, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L220).

```lean
noncomputable instance : NormedAddCommGroup (Space d)
```

**An instance with no name**, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L225).

```lean
instance {d} : Inner ℝ (Space d)
```

**`Space.inner_vadd_zero`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L229).

```lean
lemma inner_vadd_zero {d} (v1 v2 : EuclideanSpace ℝ (Fin d)) :
    inner ℝ (v1 +ᵥ (0 : Space d)) (v2 +ᵥ (0 : Space d)) = Inner.inner ℝ v1 v2
```

**`Space.inner_apply`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L233).

```lean
lemma inner_apply {d} (p q : Space d) :
    inner ℝ p q = ∑ i, p i * q i
```

**An instance with no name**, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L236).

```lean
instance {d} : InnerProductSpace ℝ (Space d)
```

**An instance with no name**, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L262).

> The normed space structure on `Space d`, registered directly. It is definitionally the
> one underlying the inner product space structure, but registering it as its own instance is
> needed for typeclass search to find the operator-norm structure on `Space d →L[ℝ] ℝ`
> (for example `NormSMulClass ℝ (Space d →L[ℝ] ℝ)`), which is not found when
> `NormedSpace ℝ (Space d)` arises only as a nested subgoal through
> `InnerProductSpace.toNormedSpace`.

```lean
noncomputable instance {d} : NormedSpace ℝ (Space d)
```

**`Space.norm_smul_sphere`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L264).

```lean
lemma norm_smul_sphere {d : ℕ} (n : ↑(Metric.sphere (0 : Space d) 1))
    {r : ℝ} (hr : 0 ≤ r) :
    ‖(r • (n : Space d))‖ = r
```

## A.4. Instance of a measurable space

**An instance with no name**, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L275).

```lean
noncomputable instance {d : ℕ} : MeasurableSpace (Space d)
```

**An instance with no name**, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L277).

```lean
instance {d : ℕ} : BorelSpace (Space d)
```

## The norm on `Space`

## Inner product

**`Space.inner_eq_sum`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L292).

```lean
lemma inner_eq_sum {d} (p q : Space d) :
    inner ℝ p q = ∑ i, p i * q i
```

**`Space.sum_apply`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L297).

```lean
lemma sum_apply {ι : Type} [Fintype ι] (f : ι → Space d) (i : Fin d) :
    (∑ x, f x) i = ∑ x, f x i
```

## Basis

> A basis in Lean is typically represented by `Module.Basis ι R M`: an indexed
> family of vectors in an `R`-module `M` such that every element of `M` has a
> unique finite linear expansion in those vectors. The index type `ι` names the
> basis vectors, and the map `basis.repr` gives the coordinate representation of a
> vector with respect to that basis.
>
> For inner product spaces, Lean also has `OrthonormalBasis ι R M`. This is a
> basis whose vectors are orthonormal, packaged together with a linear isometric
> equivalence between `M` and its coordinate space. It can be coerced to the
> underlying `Module.Basis` using `basis.toBasis` when only the linear-algebraic
> basis structure is needed.
>
> The standard basis below is indexed by `Fin d`, so the basis vector `basis i`
> is the unit vector in the `i`th coordinate direction of `Space d`.

**`Space.basis`**, a def, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L332).

> The standard basis of Space based on `Fin d`.

```lean
noncomputable def basis {d} : OrthonormalBasis (Fin d) ℝ (Space d)
```

**`Space.apply_eq_basis_repr_apply`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L352).

```lean
lemma apply_eq_basis_repr_apply {d} (p : Space d) (i : Fin d) :
    p i = basis.repr p i
```

**`Space.basis_repr_apply`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L357).

```lean
lemma basis_repr_apply {d} (p : Space d) (i : Fin d) :
    basis.repr p i = p i
```

**`Space.basis_repr_symm_apply`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L362).

```lean
lemma basis_repr_symm_apply {d} (v : EuclideanSpace ℝ (Fin d)) (i : Fin d) :
    basis.repr.symm v i = v i
```

**`Space.basis_apply`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L365).

```lean
lemma basis_apply {d} (i j : Fin d) :
    basis i j = if i = j then 1 else 0
```

**`Space.basis_self`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L370).

```lean
lemma basis_self {d} (i : Fin d) : basis i i = 1
```

**`Space.inner_basis`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L374).

```lean
lemma inner_basis {d} (p : Space d) (i : Fin d) :
    inner ℝ p (basis i) = p i
```

**`Space.basis_inner`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L379).

```lean
lemma basis_inner {d} (i : Fin d) (p : Space d) :
    inner ℝ (basis i) p = p i
```

**`Space.basis_repr_inner_eq`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L385).

```lean
lemma basis_repr_inner_eq {d} (p : Space d) (v : EuclideanSpace ℝ (Fin d)) :
    ⟪basis.repr p, v⟫_ℝ = ⟪p, basis.repr.symm v⟫_ℝ
```

**An instance with no name**, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L389).

```lean
instance {d : ℕ} : FiniteDimensional ℝ (Space d)
```

**`Space.finrank_eq_dim`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L393).

```lean
lemma finrank_eq_dim {d : ℕ} : Module.finrank ℝ (Space d) = d
```

**`Space.rank_eq_dim`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L397).

```lean
lemma rank_eq_dim {d : ℕ} : Module.rank ℝ (Space d) = d
```

**`Space.fderiv_basis_repr`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L401).

```lean
lemma fderiv_basis_repr {d} (p : Space d) :
    fderiv ℝ basis.repr p = basis.repr.toContinuousLinearMap
```

**`Space.fderiv_basis_repr_symm`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L407).

```lean
lemma fderiv_basis_repr_symm {d} (v : EuclideanSpace ℝ (Fin d)) :
    fderiv ℝ basis.repr.symm v = basis.repr.symm.toContinuousLinearMap
```

**`Space.basis_induction_on`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L412).

```lean
lemma basis_induction_on {d} {P : Space d → Prop}
    (hb : ∀ i, P (basis i)) (hzero : P 0)
    (hadd : ∀ p1 p2, P p1 → P p2 → P (p1 + p2))
    (hsmul : ∀ (c : ℝ) p, P p → P (c • p)) (p : Space d) : P p
```

## Coordinates

**`Space.coord`**, a def, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L427).

> The standard coordinate functions of Space based on `Fin d`.
>
> The notation `𝔁 μ p` can be used for this.

```lean
noncomputable def coord (μ : Fin d) (p : Space d) : ℝ
```

**`Space.coord_apply`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L430).

```lean
lemma coord_apply (μ : Fin d) (p : Space d) :
    coord μ p = p μ
```

**`Space.coordCLM`**, a def, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L435).

> The standard coordinate functions of Space based on `Fin d`, as a continuous linear map.

```lean
noncomputable def coordCLM {d} (μ : Fin d) : Space d →L[ℝ] ℝ
```

**`Space.coord_contDiff`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L448).

```lean
lemma coord_contDiff {i} : ContDiff ℝ ∞ (fun x : Space d => x.coord i)
```

**`Space.coordCLM_apply`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L451).

```lean
lemma coordCLM_apply (μ : Fin d) (p : Space d) :
    coordCLM μ p = coord μ p
```

**`Space.eval_continuous`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L459).

```lean
lemma eval_continuous {d} (i : Fin d) :
    Continuous (fun p : Space d => p i)
```

**`Space.eval_differentiable`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L465).

```lean
lemma eval_differentiable {d} (i : Fin d) :
    Differentiable ℝ (fun p : Space d => p i)
```

**`Space.eval_contDiff`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L471).

```lean
lemma eval_contDiff {d n} (i : Fin d) :
    ContDiff ℝ n (fun p : Space d => p i)
```

**`Space.eval_hasTemperateGrowth`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L477).

```lean
lemma eval_hasTemperateGrowth {d} (i : Fin d) :
    Function.HasTemperateGrowth (fun p : Space d => p i)
```

**`Space.equivPi`**, a def, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L483).

> The continuous linear equivalence between `Space d` and the corresponding `Pi` type.

```lean
noncomputable def equivPi (d : ℕ) :
    Space d ≃L[ℝ] Π (_ : Fin d), ℝ
```

## Basic differentiablity conditions

**`Space.mk_continuous`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L499).

```lean
lemma mk_continuous {d : ℕ} :
    Continuous (fun (f : Fin d → ℝ) => (⟨f⟩ : Space d))
```

**`Space.mk_differentiable`**, a lemma, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L503).

```lean
lemma mk_differentiable {d : ℕ} :
    Differentiable ℝ (fun (f : Fin d → ℝ) => (⟨f⟩ : Space d))
```

**`Space.mk_contDiff`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L507).

```lean
lemma mk_contDiff {d : ℕ} {n : WithTop ℕ∞}:
    ContDiff ℝ n (fun (f : Fin d → ℝ) => (⟨f⟩ : Space d))
```

**`Space.fderiv_mk`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L511).

```lean
lemma fderiv_mk {d : ℕ} (f : Fin d → ℝ) :
    fderiv ℝ Space.mk f = (equivPi d).symm
```

**`Space.fderiv_val`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L517).

```lean
lemma fderiv_val {d : ℕ} (p : Space d) :
    fderiv ℝ Space.val p = (equivPi d)
```

**`Space.fderiv_eval_apply`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L523).

```lean
lemma fderiv_eval_apply {d : ℕ} (p y : Space d) (i : Fin d) :
    fderiv ℝ (fun p => p.val i) p y = y i
```

**`Space.contDiffOn_vadd`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L531).

```lean
lemma contDiffOn_vadd (s : Space d) :
    ContDiffOn ℝ ω (fun (v : EuclideanSpace ℝ (Fin d)) => v +ᵥ s) Set.univ
```

**`Space.vadd_differentiable`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L536).

```lean
lemma vadd_differentiable {d} (s : Space d) :
    Differentiable ℝ (fun (v : EuclideanSpace ℝ (Fin d)) => v +ᵥ s)
```

**`Space.contDiffOn_vsub`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L541).

```lean
lemma contDiffOn_vsub (s1 : Space d) :
    ContDiffOn ℝ ω (fun (s : Space d) => s -ᵥ s1) Set.univ
```

**`Space.vsub_differentiable`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L546).

```lean
lemma vsub_differentiable {d} (s1 : Space d) :
    Differentiable ℝ (fun (s : Space d) => s -ᵥ s1)
```

**`Space.fderiv_space_components`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L550).

```lean
lemma fderiv_space_components {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin d) (f : M → Space d) (hf : Differentiable ℝ f) (m dm : M) :
    fderiv ℝ f m dm μ = fderiv ℝ (fun m' => f m' μ) m dm
```

## Directions

**`Space.Direction`**, a structure, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L568).

> Notion of direction where `unit` returns a unit vector in the direction specified.

```lean
structure Direction (d : ℕ := 3) where
  /-- Unit vector specifying the direction. -/
  unit : Space d
  norm : ‖unit‖ = 1
```

**`Space.toDirection`**, a def, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L574).

> Direction of a `Space` value with respect to the origin.

```lean
noncomputable def toDirection {d : ℕ} (x : Space d) (h : x ≠ 0) : Direction d
```

**`Space.direction_unit_sq_sum`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L579).

```lean
lemma direction_unit_sq_sum {d} (s : Direction d) :
    ∑ i : Fin d, (s.unit i) ^ 2 = 1
```

## One equiv

**`Space.oneEquiv`**, a def, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L591).

> The linear isometric equivalence between `Space 1` and `ℝ`.

```lean
noncomputable def oneEquiv : Space 1 ≃ₗᵢ[ℝ] ℝ
```

**`Space.oneEquiv_coe`**, a lemma, [line 605](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L605).

```lean
lemma oneEquiv_coe :
    (oneEquiv : Space 1 → ℝ) = fun x => x 0
```

**`Space.oneEquiv_symm_coe`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L609).

```lean
lemma oneEquiv_symm_coe :
    (oneEquiv.symm : ℝ → Space 1) = (fun x => ⟨fun _ => x⟩)
```

**`Space.oneEquiv_symm_apply`**, a lemma, [line 613](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L613).

```lean
lemma oneEquiv_symm_apply (x : ℝ) (i : Fin 1) :
    oneEquiv.symm x i = x
```

**`Space.oneEquiv_continuous`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L617).

```lean
lemma oneEquiv_continuous :
    Continuous (oneEquiv : Space 1 → ℝ)
```

**`Space.oneEquiv_symm_continuous`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L622).

```lean
lemma oneEquiv_symm_continuous :
    Continuous (oneEquiv.symm : ℝ → Space 1)
```

**`Space.oneEquivCLE`**, a def, [line 628](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L628).

> The continuous linear equivalence between `Space 1` and `ℝ`.

```lean
noncomputable def oneEquivCLE : Space 1 ≃L[ℝ] ℝ
```

**`Space.oneEquiv_measurableEmbedding`**, a lemma, [line 634](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L634).

```lean
lemma oneEquiv_measurableEmbedding : MeasurableEmbedding oneEquiv
```

**`Space.oneEquiv_symm_measurableEmbedding`**, a lemma, [line 643](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L643).

```lean
lemma oneEquiv_symm_measurableEmbedding : MeasurableEmbedding oneEquiv.symm
```

**`Space.oneEquiv_measurePreserving`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L652).

```lean
lemma oneEquiv_measurePreserving : MeasurePreserving oneEquiv volume volume
```

**`Space.oneEquiv_symm_measurePreserving`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L655).

```lean
lemma oneEquiv_symm_measurePreserving : MeasurePreserving oneEquiv.symm volume volume
```

## Relation to tangent space

**`Space.modelDiffeo`**, a def, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L667).

> A diffeomorphism between the two different manifold structures on `Space d`,
> that equivalent to `𝓡 d` and that equivalent to `𝓘(ℝ, Space d)`

```lean
noncomputable def modelDiffeo {d} : Diffeomorph (𝓡 d) 𝓘(ℝ, Space d) (Space d) (Space d) ⊤
```

**`Space.modelDiffeo_apply`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L680).

```lean
lemma modelDiffeo_apply {d : ℕ} (p : Space d) :
    modelDiffeo p = p
```

**`Space.basis_eq_mfderiv_modelDiffeo_single`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L688).

> The derivative of `modelDiffeo` provides an equivalence between
> `Space d` and `EuclideanSpace ℝ (Fin d)`. This equivalences takes the basis
> of `EuclideanSpace ℝ (Fin d)` to the basis of `Space d`, and vice versa.

```lean
lemma basis_eq_mfderiv_modelDiffeo_single (d : ℕ) (μ : Fin d) (x : Space d) :
    basis μ = mfderiv (𝓡 d) 𝓘(ℝ, Space d) (modelDiffeo (d := d)) x
      (EuclideanSpace.single μ 1)
```

## Properties of vadd with module structure

**`Space.norm_vadd_le_add`**, a lemma, [line 720](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L720).

```lean
lemma norm_vadd_le_add {d} (v : EuclideanSpace ℝ (Fin d)) (s : Space d) :
    ‖v +ᵥ s‖ ≤ ‖v‖ + ‖s‖
```

**`Space.differentiable_vadd`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L733).

```lean
lemma differentiable_vadd {d} (v : EuclideanSpace ℝ (Fin d)) :
    Differentiable ℝ (fun (s : Space d) => v +ᵥ s)
```

**`Space.fderiv_vadd`**, a lemma, [line 738](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L738).

```lean
lemma fderiv_vadd {d} (v : EuclideanSpace ℝ (Fin d)) :
    fderiv ℝ (fun s => v +ᵥ s) = fun (_ : Space d) => ContinuousLinearMap.id ℝ _
```

**`Space.vadd_hasTemperateGrowth`**, a lemma, [line 746](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean#L746).

```lean
lemma vadd_hasTemperateGrowth {d} (v : EuclideanSpace ℝ (Fin d)) :
    Function.HasTemperateGrowth (fun s : Space d => v +ᵥ s)
```

## Depends on

- [The origin of `Space` and the Euclidean chart](origin.md)

## Sources

- [Physlib/SpaceAndTime/Space/Module.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Module.lean)
