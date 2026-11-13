---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.constructibleFlatLFunction, Stacks.EtaleCohomology.EulerSystem.coeff_eulerProduct_eq, Stacks.EtaleCohomology.LAdicSheaf.rationalLFunction, Stacks.EtaleCohomology.LAdicSheaf.coeff_rationalLFunction_eq
statement: formalized
proof: formalized
---

# 64.19 L-functions

Section 64.19 of the Stacks Project, [Tag 03UU](https://stacks.math.columbia.edu/tag/03UU). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03UV, a definition

[Tag 03UV](https://stacks.math.columbia.edu/tag/03UV) in the Stacks Project.

**`Stacks.EtaleCohomology.constructibleFlatLFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FiniteCoefficientLFunction.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FiniteCoefficientLFunction.lean#L155). The attribute's comment: “the definition of L(X, F) for a constructible flat Λ-module F, for any commutative coefficient ring Λ (in particular any finite ring of order prime to the characteristic of k, local or not): the local factors are the projective determinants of the geometric Frobenius on the stalks, whose finiteness and projectivity are derived from constructible flatness; the closing remark that the definition generalizes to K in D\_ctf(X, Λ) gives no formula and is not formalized”. References: SGA 4½ Rapport (1.6), “partial”.

> The L-function `L(X, ℱ) = ∏_{x ∈ |X|} det(1 - π_x^* T ^ (deg x) |_{ℱ_x̄}) ⁻¹ ∈ Λ⟦T⟧` of a
> constructible flat `Λ`-module on `X_étale`, for a scheme of finite type over a finite field and an
> arbitrary commutative coefficient ring `Λ`, in particular any finite ring. Its local factors are
> the projective determinants of the geometric Frobenius on the finite projective stalks.

```lean
public def constructibleFlatLFunction [QuasiCompact f]
    (hF : IsConstructibleFlatModuleSheaf B X Λ F) : PowerSeries Λ
```

## Tag 03UX, a definition

[Tag 03UX](https://stacks.math.columbia.edu/tag/03UX) in the Stacks Project.

**`Stacks.EtaleCohomology.EulerSystem.coeff_eulerProduct_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LFunctionEulerProduct.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LFunctionEulerProduct.lean#L280). The attribute's comment: “the convergence of the Euler product: it is stated for an arbitrary coefficient ring, so it specializes to the Q\_ell case of this tag”.

> The Euler product converges: the coefficient of `T ^ j` of the Euler product is the
> coefficient of `T ^ j` of the product over any finite set of indices that contains all the
> indices of degree at most `j`.

```lean
public theorem coeff_eulerProduct_eq {j : ℕ} {t : Finset ι} (ht : E.support j ⊆ t) :
    PowerSeries.coeff j E.eulerProduct = PowerSeries.coeff j (∏ i ∈ t, E.factor i)
```

**`Stacks.EtaleCohomology.LAdicSheaf.rationalLFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LFunctionRationalSheaf.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LFunctionRationalSheaf.lean#L150). The attribute's comment: “the definition of L(X, F) for a Q\_ell-sheaf F, as the Euler product over the closed points of the inverse characteristic series of the geometric Frobenius on the rational stalks”. References: SGA 4½ Rapport (1.6), “adic coefficients”.

> The L-function of a `ℚ_ℓ`-sheaf `F` on a scheme `X` of finite type over a finite field `k`:
>
> `L(X, F) = ∏_{x ∈ |X|} det(1 - π_x^* T ^ (deg x) | F_x̄) ⁻¹ ∈ ℚ_ℓ⟦T⟧`,
>
> the product over the closed points `|X|` of `X` of the inverse characteristic series of the
> geometric Frobenius `π_x^*` acting on the rational stalk `F_x̄` at a geometric point over `x`,
> where `deg x = [κ(x) : k]`.  The factor at `x` is identified with
> `det(1 - π_x^* T ^ (deg x) | F_x̄) ⁻¹` by `localFactor_frobeniusMatrices`, and the product
> converges in the sense of `coeff_rationalLFunction_eq`: there are finitely many closed points of
> any given degree, so each coefficient is already computed by a finite subproduct.

```lean
public def LAdicSheaf.rationalLFunction (F : LAdicSheaf B X ℓ) (f : X.1 ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] : PowerSeries (Padic ℓ)
```

**`Stacks.EtaleCohomology.LAdicSheaf.coeff_rationalLFunction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LFunctionRationalSheaf.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LFunctionRationalSheaf.lean#L158). The attribute's comment: “the product converges since there are finitely many points of a given degree”.

> The convergence of the defining product: the coefficient of `T ^ j` of `L(X, F)` is computed
> by the product of the local factors over any finite set of closed points containing all those of
> degree at most `j`.

```lean
public theorem LAdicSheaf.coeff_rationalLFunction_eq (F : LAdicSheaf B X ℓ)
    (f : X.1 ⟶ Spec (.of k)) [LocallyOfFiniteType f] [QuasiCompact f]
    {j : ℕ} {t : Finset (closedPoints X.1)}
    (ht : (LAdicSheaf.frobeniusMatrices B X ℓ F f).eulerSystem.support j ⊆ t) :
    PowerSeries.coeff j (LAdicSheaf.rationalLFunction B X ℓ F f) =
      PowerSeries.coeff j
        (∏ x ∈ t, (LAdicSheaf.frobeniusMatrices B X ℓ F f).localFactor x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.19, Tag 03UU](https://stacks.math.columbia.edu/tag/03UU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
