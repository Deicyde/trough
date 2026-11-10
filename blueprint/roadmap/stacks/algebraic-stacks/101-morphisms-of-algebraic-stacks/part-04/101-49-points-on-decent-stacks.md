---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.t0Space_points_of_isDecent, AlgebraicGeometry.Stack.AlgebraicStacks.stacksSober_and_isLocallyNoetherianSpace_points, AlgebraicGeometry.Stack.AlgebraicStacks.stacksSober_points_of_isDecent
statement: formalized
proof: formalized
---

# 101.49 Points on decent stacks

Section 101.49 of the Stacks Project, [Tag 0GW6](https://stacks.math.columbia.edu/tag/0GW6). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GW7, a lemma

[Tag 0GW7](https://stacks.math.columbia.edu/tag/0GW7) in the Stacks Project.

**`AlgebraicGeometry.Stack.t0Space_points_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DecentStackKolmogorov.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DecentStackKolmogorov.lean#L130).

> **Stacks 0GW7.** The space of points of a decent algebraic stack over `S` is Kolmogorov: two
> points of `|𝒳|` with the same open neighbourhoods are equal.
>
> Two such points `x₁`, `x₂` have the same closure `C`, and `x₁, x₂ ∈ C`. Choose a smooth chart
> `φ : |U| → |𝒳|` by a scheme, surjective on points, and inside the nonempty closed set `φ ⁻¹' C`
> choose a point `u` maximal for specialization, which the sobriety of `|U|` provides. Decency
> feeds **Stacks 0GVZ** the quasi-compact field-valued representative it asks for, so every
> specialization `x' ⤳ φ u` with `x' ∈ C` lifts to a specialization `u' ⤳ u` with `u' ∈ φ ⁻¹' C`;
> maximality of `u` forces `u' = u` and hence `x' = φ u`. Applied to `x₁` and to `x₂`, both of
> which specialize to `φ u` because `φ u ∈ C`, this gives `x₁ = φ u = x₂`.

```lean
theorem t0Space_points_of_isDecent
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (hdecent : IsDecent B S hS 𝒳) :
    T0Space (points B S hS 𝒳.val 𝒳.property)
```

## Tag 0GW8, a lemma

[Tag 0GW8](https://stacks.math.columbia.edu/tag/0GW8) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.stacksSober_and_isLocallyNoetherianSpace_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DecentStackSober.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DecentStackSober.lean#L76).

> **Stacks 0GW8.** The space of points of Stacks 04XL of a decent, locally Noetherian
> algebraic stack over `S` is a sober, locally Noetherian topological space.
>
> Soberness is Kolmogorov together with quasi-soberness. The Kolmogorov half is Stacks 0GW7,
> which decency supplies; the quasi-sober half is Stacks 0GVX and local Noetherianity of the
> space is Stacks 0DQI, part (1), both from the locally Noetherian smooth chart of Stacks 04YF.

```lean
theorem stacksSober_and_isLocallyNoetherianSpace_points
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hdecent : Stack.IsDecent B S hS 𝒳.val)
    (hN : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳) :
    StacksSober (Stack.points B S hS 𝒳.val.val 𝒳.val.property) ∧
      IsLocallyNoetherianSpace (Stack.points B S hS 𝒳.val.val 𝒳.val.property)
```

## Tag 0GW9, a proposition

[Tag 0GW9](https://stacks.math.columbia.edu/tag/0GW9) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.stacksSober_points_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DecentStackSoberInertia.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DecentStackSoberInertia.lean#L140).

> **Stacks 0GW9.** Let `𝒳` be a decent algebraic stack over `S` such that the inertia projection
> `I_𝒳 ⟶ 𝒳` is quasi-compact. Then the space of points `|𝒳|` is sober.

```lean
theorem stacksSober_points_of_isDecent (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hd : IsDecent B S hS 𝒳.val)
    (hqc : IsQuasiCompactMorphism.{u, w} B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    @StacksSober (AlgebraicStacks.points B S hS 𝒳) (pointTopology B S hS 𝒳.val)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.49, Tag 0GW6](https://stacks.math.columbia.edu/tag/0GW6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
