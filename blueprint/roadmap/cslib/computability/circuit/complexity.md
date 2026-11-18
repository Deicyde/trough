---
catalog: module
lean: Cslib.Circuits.Interpretation.IsComplete, Cslib.Circuits.Interpretation.IsComplete.exists_computes, Cslib.Circuits.ecomplexityOn, Cslib.Circuits.ecomplexity, Cslib.Circuits.ecomplexityOn_le_of_computesOn, Cslib.Circuits.ecomplexityOn_ne_top_iff, Cslib.Circuits.exists_computesOn_size_eq_ecomplexityOn, Cslib.Circuits.ecomplexityOn_le_iff, Cslib.Circuits.le_ecomplexityOn_iff, Cslib.Circuits.ecomplexityOn_mono, Cslib.Circuits.ecomplexityOn_congr, Cslib.Circuits.ecomplexityOn_le_ecomplexity, Cslib.Circuits.ecomplexityOn_wiring, Cslib.Circuits.ecomplexityOn_comp_le, Cslib.Circuits.ecomplexityOn_append_le, Cslib.Circuits.ecomplexityOn_comp_wiring_le, Cslib.Circuits.ecomplexityOn_wiring_comp_le, Cslib.Circuits.ecomplexityOn_le_ecomplexityOn_append_left, Cslib.Circuits.ecomplexityOn_le_ecomplexityOn_append_right, Cslib.Circuits.ecomplexity_le_of_computes, Cslib.Circuits.ecomplexity_ne_top_iff, Cslib.Circuits.exists_computes_size_eq_ecomplexity, Cslib.Circuits.ecomplexity_le_iff, Cslib.Circuits.le_ecomplexity_iff, Cslib.Circuits.ecomplexity_wiring, Cslib.Circuits.ecomplexity_comp_le, Cslib.Circuits.ecomplexity_append_le, Cslib.Circuits.ecomplexity_le_ecomplexity_append_left, Cslib.Circuits.ecomplexity_le_ecomplexity_append_right, Cslib.Circuits.Synthesis.ecomplexity_le, Cslib.Circuits.ecomplexityOn_ne_top, Cslib.Circuits.ecomplexity_ne_top, Cslib.Circuits.complexityOn, Cslib.Circuits.complexity, Cslib.Circuits.natCast_complexityOn, Cslib.Circuits.natCast_complexity, Cslib.Circuits.complexityOn_le_of_computesOn, Cslib.Circuits.exists_computesOn_size_eq_complexityOn, Cslib.Circuits.complexityOn_le_iff, Cslib.Circuits.le_complexityOn_iff, Cslib.Circuits.complexity_le_of_computes, Cslib.Circuits.le_size_of_le_complexity, Cslib.Circuits.exists_computes_size_eq_complexity, Cslib.Circuits.complexity_le_iff, Cslib.Circuits.le_complexity_iff, Cslib.Circuits.complexityOn_mono, Cslib.Circuits.complexityOn_congr, Cslib.Circuits.complexityOn_le_complexity, Cslib.Circuits.complexityOn_wiring, Cslib.Circuits.complexityOn_comp_le, Cslib.Circuits.complexityOn_append_le, Cslib.Circuits.complexityOn_le_complexityOn_append_left, Cslib.Circuits.complexityOn_le_complexityOn_append_right, Cslib.Circuits.complexity_wiring, Cslib.Circuits.complexity_comp_le, Cslib.Circuits.complexity_append_le, Cslib.Circuits.complexity_le_complexity_append_left, Cslib.Circuits.complexity_le_complexity_append_right, Cslib.Circuits.Synthesis.complexity_le
statement: formalized
proof: formalized
---

# Circuit complexity

`Cslib.Computability.Circuit.Complexity`, in [Cslib/Computability/Circuit/Complexity.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean), by Samuel Schlesinger.

> The complexity of a function `f` on a support `S`, written `C^S(f)`, is the least number of gates
> in a circuit whose outputs agree with `f` on every input in `S`. The function may have several
> values, one for each output of the circuit, and nothing is asked of the circuit outside `S`, so
> `C^S(f)` depends only on the restriction of `f` to `S`. The complexity `C(f)` of `f` is its
> complexity on all inputs, and the complexity of `f` relative to a function `g`, in
> `Cslib.Computability.Circuit.RelativeComplexity`, is a complexity on the graph of `g`.
>
> Over an arbitrary signature and interpretation some functions have no circuit at all. We represent
> `C^S(f)` by `ecomplexityOn I S f` and `C(f)` by `ecomplexity I f`, taking values in `ℕ∞` with
> `⊤` when no circuit exists. The prefix `e` stands for "extended". Over a complete basis, one over
> which every function has a circuit, `complexityOn I S f` and `complexity I f` give the corresponding
> natural-number values.
>
> Support complexity obeys a small calculus from which the rules for complexity and relative
> complexity follow. It grows with the support and ignores the function outside the support.
> Wiring, which only selects, permutes, or duplicates inputs, costs nothing. The composite `g ∘ f`
> costs at most the complexity of `f` on `S` plus that of `g` on the image of `S`, and computing two
> functions side by side costs at most the sum of their complexities.
>
> See [Jukna, Chapter 1][Jukna2012] for the Boolean case.
>
> ## References
>
> * [Stasys Jukna, *Boolean Function Complexity: Advances and Frontiers*][Jukna2012]

`Cslib.Circuits.Interpretation.IsComplete` (class, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L53))

> Following [Jukna, Section 1.1][Jukna2012], a basis is complete when every single-valued
> function, on every number of inputs, is computed by some circuit over it. Circuits here have no
> constant inputs, so this includes the constants, which is why NAND alone is not complete in this
> sense. Functions with several values then have circuits too, built by running circuits for their
> values side by side.

```lean
class Interpretation.IsComplete (I : Interpretation σ U) : Prop where
  /-- Every single-valued function has a circuit. -/
  exists_computes_single :
    ∀ {n : ℕ} (f : (Fin n → U) → U), ∃ c : Circuit σ n 1, c.Computes I (single f)
```

`Cslib.Circuits.Interpretation.IsComplete.exists_computes` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L59))

> Over a complete basis every function, with any number of values, has a circuit.

```lean
theorem Interpretation.IsComplete.exists_computes {I : Interpretation σ U} [I.IsComplete] :
    ∀ {n m : ℕ} (f : (Fin n → U) → Fin m → U), ∃ c : Circuit σ n m, c.Computes I f
  | _, 0, _ => ⟨Circuit.wiring σ Fin.elim0, fun _ => funext fun i => i.elim0⟩
  | _, m + 1, f => by
    obtain ⟨c, hc⟩
```

`Cslib.Circuits.ecomplexityOn` (definition, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L71))

> The complexity `C^S(f)` of `f` on the support `S`: the least size of a circuit computing `f`
> on `S` under `I`, or `⊤` if there is none.

```lean
noncomputable def ecomplexityOn (I : Interpretation σ U) (S : Set (Fin n → U))
    (f : (Fin n → U) → Fin m → U) : ℕ∞
```

`Cslib.Circuits.ecomplexity` (definition, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L76))

> The complexity `C(f)` of `f`: its complexity on all inputs.

```lean
noncomputable def ecomplexity (I : Interpretation σ U) (f : (Fin n → U) → Fin m → U) : ℕ∞
```

> ### Complexity on a support

`Cslib.Circuits.ecomplexityOn_le_of_computesOn` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L84))

```lean
theorem ecomplexityOn_le_of_computesOn (c : Circuit σ n m) (hc : c.ComputesOn I S f) :
    ecomplexityOn I S f ≤ c.size
```

`Cslib.Circuits.ecomplexityOn_ne_top_iff` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L88))

```lean
theorem ecomplexityOn_ne_top_iff :
    ecomplexityOn I S f ≠ ⊤ ↔ ∃ c : Circuit σ n m, c.ComputesOn I S f
```

`Cslib.Circuits.exists_computesOn_size_eq_ecomplexityOn` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L94))

> When some circuit computes `f` on `S`, the least size is attained by some
> (potentially different) circuit.

```lean
theorem exists_computesOn_size_eq_ecomplexityOn (h : ∃ c : Circuit σ n m, c.ComputesOn I S f) :
    ∃ c : Circuit σ n m, c.ComputesOn I S f ∧ (c.size : ℕ∞) = ecomplexityOn I S f
```

`Cslib.Circuits.ecomplexityOn_le_iff` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L101))

```lean
theorem ecomplexityOn_le_iff :
    ecomplexityOn I S f ≤ k ↔ ∃ c : Circuit σ n m, c.ComputesOn I S f ∧ c.size ≤ k
```

`Cslib.Circuits.le_ecomplexityOn_iff` (theorem, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L114))

> Lower bounds on support complexity are exactly lower bounds on the size of every circuit
> computing the function on the support, including when no such circuit exists.

```lean
theorem le_ecomplexityOn_iff {k : ℕ∞} :
    k ≤ ecomplexityOn I S f ↔
      ∀ c : Circuit σ n m, c.ComputesOn I S f → k ≤ c.size
```

`Cslib.Circuits.ecomplexityOn_mono` (theorem, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L120))

> A larger support is harder to compute on.

```lean
theorem ecomplexityOn_mono (h : S ⊆ T) : ecomplexityOn I S f ≤ ecomplexityOn I T f
```

`Cslib.Circuits.ecomplexityOn_congr` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L124))

> Complexity on a support depends only on the values of the function on the support.

```lean
theorem ecomplexityOn_congr (h : Set.EqOn f f' S) : ecomplexityOn I S f = ecomplexityOn I S f'
```

`Cslib.Circuits.ecomplexityOn_le_ecomplexity` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L128))

```lean
theorem ecomplexityOn_le_ecomplexity : ecomplexityOn I S f ≤ ecomplexity I f
```

`Cslib.Circuits.ecomplexityOn_wiring` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L132))

> Selecting, permuting, or duplicating inputs costs nothing.

```lean
theorem ecomplexityOn_wiring (select : Fin m → Fin n) :
    ecomplexityOn I S (fun x => x ∘ select) = 0
```

`Cslib.Circuits.ecomplexityOn_comp_le` (theorem, [line 139](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L139))

> The composition rule: computing `g ∘ f` on `S` costs at most computing `f` on `S` and then
> `g` on the values `f` takes there.

```lean
theorem ecomplexityOn_comp_le (f : (Fin n → U) → Fin m → U) (g : (Fin m → U) → Fin p → U) :
    ecomplexityOn I S (g ∘ f) ≤ ecomplexityOn I S f + ecomplexityOn I (f '' S) g
```

`Cslib.Circuits.ecomplexityOn_append_le` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L152))

> The pairing rule: computing `f` and `g` side by side on `S` costs at most the sum of their
> complexities on `S`.

```lean
theorem ecomplexityOn_append_le (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin p → U) :
    ecomplexityOn I S (fun x => Fin.append (f x) (g x)) ≤
      ecomplexityOn I S f + ecomplexityOn I S g
```

`Cslib.Circuits.ecomplexityOn_comp_wiring_le` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L166))

> Reading the inputs through a wiring costs nothing beyond computing `f` on the rewired
> support.

```lean
theorem ecomplexityOn_comp_wiring_le {S : Set (Fin p → U)} (select : Fin n → Fin p)
    (f : (Fin n → U) → Fin m → U) :
    ecomplexityOn I S (fun x => f (x ∘ select)) ≤ ecomplexityOn I ((· ∘ select) '' S) f
```

`Cslib.Circuits.ecomplexityOn_wiring_comp_le` (theorem, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L174))

> Selecting, permuting, or duplicating the values of `f` costs nothing.

```lean
theorem ecomplexityOn_wiring_comp_le (select : Fin p → Fin m) (f : (Fin n → U) → Fin m → U) :
    ecomplexityOn I S (fun x => f x ∘ select) ≤ ecomplexityOn I S f
```

`Cslib.Circuits.ecomplexityOn_le_ecomplexityOn_append_left` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L181))

> Computing `f` alongside `g` on `S` is at least as hard as computing `f` on `S`.

```lean
theorem ecomplexityOn_le_ecomplexityOn_append_left (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    ecomplexityOn I S f ≤ ecomplexityOn I S (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.ecomplexityOn_le_ecomplexityOn_append_right` (theorem, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L189))

> Computing `g` alongside `f` on `S` is at least as hard as computing `g` on `S`.

```lean
theorem ecomplexityOn_le_ecomplexityOn_append_right (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    ecomplexityOn I S g ≤ ecomplexityOn I S (fun x => Fin.append (f x) (g x))
```

> ### Complexity on all inputs

`Cslib.Circuits.ecomplexity_le_of_computes` (theorem, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L198))

```lean
theorem ecomplexity_le_of_computes (c : Circuit σ n m) (hc : c.Computes I f) :
    ecomplexity I f ≤ c.size
```

`Cslib.Circuits.ecomplexity_ne_top_iff` (theorem, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L202))

```lean
theorem ecomplexity_ne_top_iff : ecomplexity I f ≠ ⊤ ↔ ∃ c : Circuit σ n m, c.Computes I f
```

`Cslib.Circuits.exists_computes_size_eq_ecomplexity` (theorem, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L207))

> When some circuit computes `f`, the least size is attained by some (potentially different)
> circuit.

```lean
theorem exists_computes_size_eq_ecomplexity (h : ∃ c : Circuit σ n m, c.Computes I f) :
    ∃ c : Circuit σ n m, c.Computes I f ∧ (c.size : ℕ∞) = ecomplexity I f
```

`Cslib.Circuits.ecomplexity_le_iff` (theorem, [line 213](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L213))

```lean
theorem ecomplexity_le_iff :
    ecomplexity I f ≤ k ↔ ∃ c : Circuit σ n m, c.Computes I f ∧ c.size ≤ k
```

`Cslib.Circuits.le_ecomplexity_iff` (theorem, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L219))

> Lower bounds on complexity are exactly lower bounds on the size of every circuit computing
> the function, including when no such circuit exists.

```lean
theorem le_ecomplexity_iff {k : ℕ∞} :
    k ≤ ecomplexity I f ↔ ∀ c : Circuit σ n m, c.Computes I f → k ≤ c.size
```

`Cslib.Circuits.ecomplexity_wiring` (theorem, [line 224](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L224))

> Selecting, permuting, or duplicating inputs costs nothing.

```lean
theorem ecomplexity_wiring (select : Fin m → Fin n) :
    ecomplexity I (fun x => x ∘ select) = 0
```

`Cslib.Circuits.ecomplexity_comp_le` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L228))

```lean
theorem ecomplexity_comp_le (f : (Fin n → U) → Fin m → U) (g : (Fin m → U) → Fin p → U) :
    ecomplexity I (g ∘ f) ≤ ecomplexity I f + ecomplexity I g
```

`Cslib.Circuits.ecomplexity_append_le` (theorem, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L232))

```lean
theorem ecomplexity_append_le (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin p → U) :
    ecomplexity I (fun x => Fin.append (f x) (g x)) ≤ ecomplexity I f + ecomplexity I g
```

`Cslib.Circuits.ecomplexity_le_ecomplexity_append_left` (theorem, [line 237](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L237))

> Computing `f` alongside `g` is at least as hard as computing `f`.

```lean
theorem ecomplexity_le_ecomplexity_append_left (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    ecomplexity I f ≤ ecomplexity I (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.ecomplexity_le_ecomplexity_append_right` (theorem, [line 243](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L243))

> Computing `g` alongside `f` is at least as hard as computing `g`.

```lean
theorem ecomplexity_le_ecomplexity_append_right (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    ecomplexity I g ≤ ecomplexity I (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.Synthesis.ecomplexity_le` (theorem, [line 249](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L249))

> A synthesis bound on the input projections bounds the extended complexity.

```lean
theorem Synthesis.ecomplexity_le {f : (Fin n → U) → U} {cost : ℕ}
    (h : Synthesis I (inputs n) {f} cost) : ecomplexity I (single f) ≤ cost
```

> ### Over a complete basis

`Cslib.Circuits.ecomplexityOn_ne_top` (theorem, [line 257](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L257))

```lean
theorem ecomplexityOn_ne_top [I.IsComplete] : ecomplexityOn I S f ≠ ⊤
```

`Cslib.Circuits.ecomplexity_ne_top` (theorem, [line 261](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L261))

```lean
theorem ecomplexity_ne_top [I.IsComplete] : ecomplexity I f ≠ ⊤
```

`Cslib.Circuits.complexityOn` (definition, [line 266](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L266))

> The complexity `C^S(f)` of `f` on the support `S` over a complete basis, as a natural
> number.

```lean
noncomputable def complexityOn (I : Interpretation σ U) [I.IsComplete] (S : Set (Fin n → U))
    (f : (Fin n → U) → Fin m → U) : ℕ
```

`Cslib.Circuits.complexity` (definition, [line 271](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L271))

> The complexity `C(f)` of `f` over a complete basis, as a natural number.

```lean
noncomputable def complexity (I : Interpretation σ U) [I.IsComplete]
    (f : (Fin n → U) → Fin m → U) : ℕ
```

`Cslib.Circuits.natCast_complexityOn` (theorem, [line 277](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L277))

```lean
theorem natCast_complexityOn : (complexityOn I S f : ℕ∞) = ecomplexityOn I S f
```

`Cslib.Circuits.natCast_complexity` (theorem, [line 280](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L280))

```lean
theorem natCast_complexity : (complexity I f : ℕ∞) = ecomplexity I f
```

`Cslib.Circuits.complexityOn_le_of_computesOn` (theorem, [line 284](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L284))

> A circuit computing `f` on `S` bounds its support complexity.

```lean
theorem complexityOn_le_of_computesOn (c : Circuit σ n m) (hc : c.ComputesOn I S f) :
    complexityOn I S f ≤ c.size
```

`Cslib.Circuits.exists_computesOn_size_eq_complexityOn` (theorem, [line 291](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L291))

> Over a complete basis the least size on a support is attained.

```lean
theorem exists_computesOn_size_eq_complexityOn :
    ∃ c : Circuit σ n m, c.ComputesOn I S f ∧ c.size = complexityOn I S f
```

`Cslib.Circuits.complexityOn_le_iff` (theorem, [line 299](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L299))

> Support complexity is at most `k` exactly when some circuit of size at most `k` computes
> the function on the support.

```lean
theorem complexityOn_le_iff :
    complexityOn I S f ≤ k ↔ ∃ c : Circuit σ n m, c.ComputesOn I S f ∧ c.size ≤ k
```

`Cslib.Circuits.le_complexityOn_iff` (theorem, [line 306](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L306))

> Over a complete basis, lower bounds on support complexity are exactly lower bounds on the
> size of every circuit computing the function on the support.

```lean
theorem le_complexityOn_iff :
    k ≤ complexityOn I S f ↔ ∀ c : Circuit σ n m, c.ComputesOn I S f → k ≤ c.size
```

`Cslib.Circuits.complexity_le_of_computes` (theorem, [line 312](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L312))

```lean
theorem complexity_le_of_computes (c : Circuit σ n m) (hc : c.Computes I f) :
    complexity I f ≤ c.size
```

`Cslib.Circuits.le_size_of_le_complexity` (theorem, [line 317](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L317))

> A lower bound on the complexity is a lower bound on the size of every circuit.

```lean
theorem le_size_of_le_complexity (h : k ≤ complexity I f) {c : Circuit σ n m}
    (hc : c.Computes I f) : k ≤ c.size
```

`Cslib.Circuits.exists_computes_size_eq_complexity` (theorem, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L322))

> Over a complete basis the least size is attained.

```lean
theorem exists_computes_size_eq_complexity :
    ∃ c : Circuit σ n m, c.Computes I f ∧ c.size = complexity I f
```

`Cslib.Circuits.complexity_le_iff` (theorem, [line 327](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L327))

```lean
theorem complexity_le_iff :
    complexity I f ≤ k ↔ ∃ c : Circuit σ n m, c.Computes I f ∧ c.size ≤ k
```

`Cslib.Circuits.le_complexity_iff` (theorem, [line 333](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L333))

> Over a complete basis, lower bounds on complexity are exactly lower bounds on the size
> of every circuit.

```lean
theorem le_complexity_iff :
    k ≤ complexity I f ↔ ∀ c : Circuit σ n m, c.Computes I f → k ≤ c.size
```

`Cslib.Circuits.complexityOn_mono` (theorem, [line 337](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L337))

```lean
theorem complexityOn_mono (h : S ⊆ T) : complexityOn I S f ≤ complexityOn I T f
```

`Cslib.Circuits.complexityOn_congr` (theorem, [line 343](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L343))

> Complexity on a support depends only on the values of the function on the support.

```lean
theorem complexityOn_congr (h : Set.EqOn f f' S) : complexityOn I S f = complexityOn I S f'
```

`Cslib.Circuits.complexityOn_le_complexity` (theorem, [line 349](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L349))

> Restricting the inputs to a support cannot increase complexity.

```lean
theorem complexityOn_le_complexity : complexityOn I S f ≤ complexity I f
```

`Cslib.Circuits.complexityOn_wiring` (theorem, [line 353](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L353))

> Selecting, permuting, or duplicating inputs costs nothing.

```lean
theorem complexityOn_wiring (select : Fin m → Fin n) :
    complexityOn I S (fun x => x ∘ select) = 0
```

`Cslib.Circuits.complexityOn_comp_le` (theorem, [line 359](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L359))

```lean
theorem complexityOn_comp_le (f : (Fin n → U) → Fin m → U) (g : (Fin m → U) → Fin p → U) :
    complexityOn I S (g ∘ f) ≤ complexityOn I S f + complexityOn I (f '' S) g
```

`Cslib.Circuits.complexityOn_append_le` (theorem, [line 365](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L365))

```lean
theorem complexityOn_append_le (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin p → U) :
    complexityOn I S (fun x => Fin.append (f x) (g x)) ≤
      complexityOn I S f + complexityOn I S g
```

`Cslib.Circuits.complexityOn_le_complexityOn_append_left` (theorem, [line 373](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L373))

> Computing `f` alongside `g` on `S` is at least as hard as computing `f` on `S`.

```lean
theorem complexityOn_le_complexityOn_append_left (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    complexityOn I S f ≤ complexityOn I S (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.complexityOn_le_complexityOn_append_right` (theorem, [line 381](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L381))

> Computing `g` alongside `f` on `S` is at least as hard as computing `g` on `S`.

```lean
theorem complexityOn_le_complexityOn_append_right (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    complexityOn I S g ≤ complexityOn I S (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.complexity_wiring` (theorem, [line 389](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L389))

> Selecting, permuting, or duplicating inputs costs nothing.

```lean
theorem complexity_wiring (select : Fin m → Fin n) :
    complexity I (fun x => x ∘ select) = 0
```

`Cslib.Circuits.complexity_comp_le` (theorem, [line 394](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L394))

> Computing a composite costs at most the sum of the complexities of its two functions.

```lean
theorem complexity_comp_le (f : (Fin n → U) → Fin m → U) (g : (Fin m → U) → Fin p → U) :
    complexity I (g ∘ f) ≤ complexity I f + complexity I g
```

`Cslib.Circuits.complexity_append_le` (theorem, [line 399](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L399))

> Computing two functions side by side costs at most the sum of their complexities.

```lean
theorem complexity_append_le (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin p → U) :
    complexity I (fun x => Fin.append (f x) (g x)) ≤ complexity I f + complexity I g
```

`Cslib.Circuits.complexity_le_complexity_append_left` (theorem, [line 404](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L404))

> Computing `f` alongside `g` is at least as hard as computing `f`.

```lean
theorem complexity_le_complexity_append_left (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    complexity I f ≤ complexity I (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.complexity_le_complexity_append_right` (theorem, [line 410](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L410))

> Computing `g` alongside `f` is at least as hard as computing `g`.

```lean
theorem complexity_le_complexity_append_right (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin p → U) :
    complexity I g ≤ complexity I (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.Synthesis.complexity_le` (theorem, [line 416](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean#L416))

> A synthesis bound on the input projections bounds the complexity.

```lean
theorem Synthesis.complexity_le {f : (Fin n → U) → U} {cost : ℕ}
    (h : Synthesis I (inputs n) {f} cost) : complexity I (single f) ≤ cost
```

## Depends on

- [Simultaneous circuit synthesis](synthesis.md)

## Proof depends on

- [Composing circuits](composition.md)

## Sources

- [Cslib/Computability/Circuit/Complexity.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Complexity.lean)
