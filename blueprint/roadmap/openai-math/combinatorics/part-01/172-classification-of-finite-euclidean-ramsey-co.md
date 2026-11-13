---
declaration: section
origin: cited
lean: OAI.EuclideanRamsey.classification, OAI.GrahamSpherical.full_main, OAI.EuclideanRamsey.CircleConsequence.at_most_five_circle_points_ramsey, OAI.EuclideanRamsey.NineStatement.nine_circle_configuration, OAI.EuclideanRamsey.spherical_quadraticIndependent_ramsey_all, OAI.EuclideanRamsey.ramsey_cospherical, OAI.EuclideanRamsey.TransitiveConsequence.subset_of_finite_transitive_ramsey
statement: formalized
proof: formalized
---

# 172. Classification of finite Euclidean Ramsey configurations

1 manuscript and 7 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Classifies finite point configurations that occur monochromatically, at their original scale, in every finite coloring of sufficiently high-dimensional Euclidean space. The characterization is an algebraic condition over the coordinate field. It also disproves the Leader–Russell–Walters conjecture that every such configuration is a subset of a finite transitive set.

## A classification of finite Euclidean Ramsey configurations

We classify finite Euclidean Ramsey configurations by a necessary and sufficient tensor condition over their coordinate fields. The Ramsey property here concerns monochromatic congruent copies at the original scale under arbitrary finite colorings. The criterion shows that every nonempty subtransitive set and every nonempty set of at most five points on a circle is Ramsey. In particular, some Ramsey cyclic quadrilaterals are not subtransitive, disproving the necessity direction of the Leader–Russell–Walters conjectured characterization.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

A finite configuration is Euclidean Ramsey if every finite coloring of some sufficiently high-dimensional Euclidean space contains a monochromatic congruent copy at the original scale. The formalization gives the tensor-field classification for full-affine-span configurations, covers singleton and affine-span reductions, and proves that every Ramsey configuration is cospherical. It also proves that every nonempty subset of a finite transitive configuration and every nonempty set of at most five points on a circle is Ramsey. A further sufficient condition uses linear independence of the quadratic evaluation rows of a spherical configuration.

The formalization also gives spherical non-Ramsey examples: the specified twelve-point set on the unit circle has a fifty-color obstruction in every positive dimension, and a nine-point circle configuration built from algebraically independent parameters is non-Ramsey.

## Lean: Tensor-field classification of Ramsey configurations

```lean
theorem classification {s d : ℕ} (a : Fin s → Space d)
    (hs : 2 ≤ s) (hd : 1 ≤ d) (ha : Function.Injective a)
    (hspan : affineSpan ℝ (Set.range a) = ⊤) :
    Ramsey a ↔ FieldCriterion a
```

Stated in [EuclideanRamsey.lean, line 42](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanRamsey.lean#L42). Proved in [lean/OAI/Combinatorics/EuclideanRamsey/Main.lean, line 69](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EuclideanRamsey/Main.lean#L69). formalization.yaml lists it as one of the repository's main results.

## Lean: Twelve-point spherical non-Ramsey example

```lean
theorem full_main : Specification.FullAuthoredResult
```

Stated in [GrahamSpherical.lean, line 58](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GrahamSpherical.lean#L58). Proved in [lean/OAI/Combinatorics/SphericalRamsey/Main.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/SphericalRamsey/Main.lean#L23). formalization.yaml lists it as one of the repository's main results.

## Lean: Ramsey property for at most five circle points

```lean
theorem at_most_five_circle_points_ramsey {s : ℕ} (a : Fin s → Space 2)
    (hs : 0 < s) (hs5 : s ≤ 5) (ha : Function.Injective a)
    (hsphere : ∃ c : Space 2, ∃ r : ℝ, ∀ i, dist (a i) c = r) : Ramsey a
```

Stated in [EuclideanRamseyCircle.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanRamseyCircle.lean#L21). Proved in [lean/OAI/Combinatorics/EuclideanRamsey/Circle.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EuclideanRamsey/Circle.lean#L21).

## Lean: Nine-point non-Ramsey circle configuration

```lean
theorem nine_circle_configuration (t : Fin 9 → ℝ)
    (ht : AlgebraicIndependent ℚ t) :
    Function.Injective (literalCircleConfig t) ∧
      (∀ i, dist (literalCircleConfig t i) 0 = 1) ∧
      ¬ Ramsey (literalCircleConfig t)
```

Stated in [EuclideanRamseyNine.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanRamseyNine.lean#L26). Proved in [lean/OAI/Combinatorics/EuclideanRamsey/NineStatement.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EuclideanRamsey/NineStatement.lean#L24).

## Lean: Quadratic-independence criterion for spherical configurations

```lean
theorem spherical_quadraticIndependent_ramsey_all {s d : ℕ}
    (a : Fin s → Space d) (ha : Function.Injective a)
    (hspan : affineSpan ℝ (Set.range a) = ⊤)
    (hsphere : ∃ c : Space d, ∃ r : ℝ, ∀ i, dist (a i) c = r)
    (hrows : LinearIndependent (Coeff a)
      (fun i : Fin s => fun q : Option (Fin d) × Option (Fin d) =>
        augmented a i q.1 * augmented a i q.2)) : Ramsey a
```

Stated in [EuclideanRamseyQuadratic.lean, line 31](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanRamseyQuadratic.lean#L31). Proved in [lean/OAI/Combinatorics/EuclideanRamsey/Quadratic.lean, line 253](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EuclideanRamsey/Quadratic.lean#L253).

## Lean: Cosphericity of Ramsey configurations

```lean
theorem ramsey_cospherical {s d : ℕ} (a : Fin s → Space d)
    (ha : Function.Injective a) (hR : Ramsey a) :
    EuclideanGeometry.Cospherical (Set.range a)
```

Stated in [EuclideanRamseySpherical.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanRamseySpherical.lean#L19). Proved in [lean/OAI/Combinatorics/EuclideanRamsey/Spherical.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EuclideanRamsey/Spherical.lean#L15).

## Lean: Ramsey property for subsets of finite transitive configurations

```lean
theorem subset_of_finite_transitive_ramsey {s t D : ℕ}
    (a : Fin s → Space D) (y : Fin t → Space D)
    (hs : 0 < s) (ha : Function.Injective a) (_hy : Function.Injective y)
    (htrans : ∀ i j : Fin t, ∃ σ : Equiv.Perm (Fin t),
      (∀ k l : Fin t, dist (y (σ k)) (y (σ l)) = dist (y k) (y l)) ∧ σ i = j)
    (hsub : Set.range a ⊆ Set.range y) : Ramsey a
```

Stated in [EuclideanRamseyTransitive.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanRamseyTransitive.lean#L19). Proved in [lean/OAI/Combinatorics/EuclideanRamsey/Transitive.lean, line 136](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/EuclideanRamsey/Transitive.lean#L136).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/172.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/172.md)
