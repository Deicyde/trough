# Hadamard three-lines theorem

**Hadamard three-line theorem**: If `f` is a bounded function, continuous on the
closed strip `re ⁻¹' [l, u]` and differentiable on open strip `re ⁻¹' (l, u)`, then for
`M(x) := sup ((norm ∘ f) '' re ⁻¹' {x})` we have that for all `z` in the closed strip
`re ⁻¹' [a,b]` the inequality
`‖f(z)‖ ≤ M(0) ^ (1 - ((z.re - l) / (u - l))) * M(1) ^ ((z.re - l) / (u - l))`
holds.

```lean
Complex.HadamardThreeLines.norm_le_interpStrip_of_mem_verticalClosedStrip.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {l u : ℝ} (hul : l < u) {f : ℂ → E} {z : ℂ}
  (hz : z ∈ Complex.HadamardThreeLines.verticalClosedStrip l u)
  (hd : DiffContOnCl ℂ f (Complex.HadamardThreeLines.verticalStrip l u))
  (hB : BddAbove (norm ∘ f '' Complex.HadamardThreeLines.verticalClosedStrip l u)) :
  ‖f z‖ ≤ ‖Complex.HadamardThreeLines.interpStrip' f l u z‖
```

## Depends on

- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Holomorphic functions](../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Phragmen-Lindelöf principle](../../../overview/analysis/complex-analysis/phragmen-lindelof-principle.md)

## Sources

- [Mathlib documentation: `Complex.HadamardThreeLines.norm_le_interpStrip_of_mem_verticalClosedStrip`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Hadamard.html#Complex.HadamardThreeLines.norm_le_interpStrip_of_mem_verticalClosedStrip)
- [Source of `Complex.HadamardThreeLines.norm_le_interpStrip_of_mem_verticalClosedStrip` in Mathlib/Analysis/Complex/Hadamard.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Complex/Hadamard.lean#L585)
- [1000+ theorems list: Q3527250](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2586)
- [1000+ theorems project: Q3527250](https://1000-plus.github.io/all.html?length=-1#Q3527250)
- [Wikipedia: Hadamard three-lines theorem](https://en.wikipedia.org/wiki/Hadamard_three-lines_theorem)
- [Wikidata: Q3527250](https://www.wikidata.org/wiki/Q3527250)
