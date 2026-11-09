# Theorem of Ceva

**Ceva's theorem** for a triangle, expressed using division of distances.

```lean
Affine.Triangle.prod_dist_div_dist_eq_one_of_mem_line_of_mem_line.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {V : Type u_2} {P : Type u_3} [SeminormedAddCommGroup V] [NormedField 𝕜] [NormedSpace 𝕜 V]
  [MetricSpace P] [NormedAddTorsor V P] {t : Affine.Triangle 𝕜 P} {p : Fin 3 → P} {p' : P}
  (hp0 : ∀ (i : Fin 3), p i ≠ t.points (i + 2))
  (hp : ∀ (i : Fin 3), p i ∈ line[𝕜, t.points (i + 1), t.points (i + 2)])
  (hp' : ∀ (i : Fin 3), p' ∈ line[𝕜, t.points i, p i]) :
  ∏ i, dist (t.points (i + 1)) (p i) / dist (p i) (t.points (i + 2)) = 1
```

## Depends on

- [Affine span](../../overview/geometry/affine-and-euclidean-geometry/affine-span.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Linear map](../../overview/linear-algebra/fundamentals/linear-map.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)

## Sources

- [Mathlib documentation: `Affine.Triangle.prod_dist_div_dist_eq_one_of_mem_line_of_mem_line`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Affine/Ceva.html#Affine.Triangle.prod_dist_div_dist_eq_one_of_mem_line_of_mem_line)
- [Source of `Affine.Triangle.prod_dist_div_dist_eq_one_of_mem_line_of_mem_line` in Mathlib/Analysis/Normed/Affine/Ceva.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Affine/Ceva.lean#L44)
- [Freek Wiedijk's 100 theorems, no. 61](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L311)
- [1000+ theorems list: Q213603](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L233)
- [1000+ theorems project: Q213603](https://1000-plus.github.io/all.html?length=-1#Q213603)
- [Wikipedia: Ceva's theorem](https://en.wikipedia.org/wiki/Ceva's_theorem)
- [Wikidata: Q213603](https://www.wikidata.org/wiki/Q213603)
