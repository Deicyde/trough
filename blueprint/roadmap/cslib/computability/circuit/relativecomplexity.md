---
catalog: module
lean: Cslib.Circuits.graph, Cslib.Circuits.onFirstInputs, Cslib.Circuits.ecomplexityGiven, Cslib.Circuits.Circuit.computesOn_graph_iff, Cslib.Circuits.ecomplexityGiven_le_of_eval, Cslib.Circuits.ecomplexityGiven_le_iff, Cslib.Circuits.ecomplexity_append_self_le, Cslib.Circuits.ecomplexityGiven_self, Cslib.Circuits.ecomplexityGiven_le_ecomplexity, Cslib.Circuits.ecomplexity_le_add_ecomplexityGiven, Cslib.Circuits.ecomplexity_append_le_add_ecomplexityGiven, Cslib.Circuits.ecomplexityGiven_le_add, Cslib.Circuits.ecomplexityGiven_append_le, Cslib.Circuits.ecomplexityGiven_ne_top, Cslib.Circuits.complexityGiven, Cslib.Circuits.natCast_complexityGiven, Cslib.Circuits.complexityGiven_self, Cslib.Circuits.complexityGiven_le_complexity, Cslib.Circuits.complexity_le_add_complexityGiven, Cslib.Circuits.complexity_append_le_add_complexityGiven, Cslib.Circuits.complexityGiven_le_add, Cslib.Circuits.complexityGiven_append_le
statement: formalized
proof: formalized
---

# Relative circuit complexity

`Cslib.Computability.Circuit.RelativeComplexity`, in [Cslib/Computability/Circuit/RelativeComplexity.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean), by Samuel Schlesinger.

> The complexity `C(f | g)` of `f` relative to `g` is the least number of gates needed to compute
> `f` when the values of `g` come for free: the circuit reads an input `x` followed by the values
> `g x`. Such a circuit only ever sees inputs of this form, which make up the graph of `g`, so
> computing `f` given `g` is computing `f` of the first part of the input, on the graph of `g`.
> Relative complexity is defined as this complexity on a support, `C(f | g) = C^Γ(f ∘ π)` where
> `Γ` is the graph of `g` and `π` forgets the values of `g`. The reading in terms of circuits on
> `x` and `g x` is recovered by `ecomplexityGiven_le_iff`.
>
> The rules of relative complexity follow from the calculus of support complexity. Knowing `g`
> never makes `f` harder, and knowing more never makes it harder either.
> Computing `g` and then `f` from it gives the chain rule `C(f) ≤ C(g) + C(f | g)`, and its
> variant for computing `f` and `g` together. Relative complexity satisfies the triangle
> inequality `C(f | h) ≤ C(g | h) + C(f | g)`, and every function is free given itself.

`Cslib.Circuits.graph` (definition, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L36))

> The graph of `g`: every input followed by the values of `g` on it.

```lean
def graph (g : (Fin n → U) → Fin k → U) : Set (Fin (n + k) → U)
```

`Cslib.Circuits.onFirstInputs` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L40))

> Apply `f` to the first `n` inputs, ignoring the last `k` inputs.

```lean
def onFirstInputs (k : ℕ) (f : (Fin n → U) → Fin m → U) : (Fin (n + k) → U) → Fin m → U
```

`Cslib.Circuits.ecomplexityGiven` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L48))

> The complexity `C(f | g)` of `f` relative to `g`: the least size of a single circuit satisfying
> `c.eval I (Fin.append x (g x)) = f x` for every `x`, or `⊤` if there is none.
> Each evaluation supplies only `x` and `g x`; values of `g` at other inputs are not provided.
> `graph g` specifies the inputs on which the circuit must be correct, and `onFirstInputs k f`
> specifies its required output on those inputs.

```lean
noncomputable def ecomplexityGiven (I : Interpretation σ U) (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) : ℕ∞
```

`Cslib.Circuits.Circuit.computesOn_graph_iff` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L56))

> A circuit computes `f` of the first `n` inputs on the graph of `g` exactly when, reading an
> input followed by the values of `g` on it, it outputs the values of `f` on that input.

```lean
theorem Circuit.computesOn_graph_iff {f : (Fin n → U) → Fin m → U} {g : (Fin n → U) → Fin k → U}
    (c : Circuit σ (n + k) m) :
    c.ComputesOn I (graph g) (onFirstInputs k f) ↔
      ∀ x, c.eval I (Fin.append x (g x)) = f x
```

`Cslib.Circuits.ecomplexityGiven_le_of_eval` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L66))

```lean
theorem ecomplexityGiven_le_of_eval (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin k → U)
    (c : Circuit σ (n + k) m) (hc : ∀ x, c.eval I (Fin.append x (g x)) = f x) :
    ecomplexityGiven I f g ≤ c.size
```

`Cslib.Circuits.ecomplexityGiven_le_iff` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L71))

```lean
theorem ecomplexityGiven_le_iff (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin k → U) :
    ecomplexityGiven I f g ≤ s ↔
      ∃ c : Circuit σ (n + k) m, (∀ x, c.eval I (Fin.append x (g x)) = f x) ∧ c.size ≤ s
```

`Cslib.Circuits.ecomplexity_append_self_le` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L77))

> Computing the graph map `x ↦ (x, g x)` costs no more than computing `g`.

```lean
theorem ecomplexity_append_self_le (g : (Fin n → U) → Fin k → U) :
    ecomplexity I (fun x => Fin.append x (g x)) ≤ ecomplexity I g
```

`Cslib.Circuits.ecomplexityGiven_self` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L84))

> Every function is free given itself: `C(f | f) = 0`.

```lean
theorem ecomplexityGiven_self (f : (Fin n → U) → Fin m → U) :
ecomplexityGiven I f f = 0
```

`Cslib.Circuits.ecomplexityGiven_le_ecomplexity` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L92))

> Knowing `g` never makes `f` harder: `C(f | g) ≤ C(f)`.

```lean
theorem ecomplexityGiven_le_ecomplexity (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) : ecomplexityGiven I f g ≤ ecomplexity I f
```

`Cslib.Circuits.ecomplexity_le_add_ecomplexityGiven` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L98))

> The chain rule: computing `g` and then `f` from it gives `C(f) ≤ C(g) + C(f | g)`.

```lean
theorem ecomplexity_le_add_ecomplexityGiven (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) :
    ecomplexity I f ≤ ecomplexity I g + ecomplexityGiven I f g
```

`Cslib.Circuits.ecomplexity_append_le_add_ecomplexityGiven` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L119))

> Computing `f` and `g` together costs at most computing `f` and then `g` given `f`.

```lean
theorem ecomplexity_append_le_add_ecomplexityGiven (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) :
    ecomplexity I (fun x => Fin.append (f x) (g x)) ≤ ecomplexity I f + ecomplexityGiven I g f
```

`Cslib.Circuits.ecomplexityGiven_le_add` (theorem, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L149))

> The triangle inequality: `C(f | h) ≤ C(g | h) + C(f | g)`. Given `h`, compute `g`, and then
> `f` from `g`.

```lean
theorem ecomplexityGiven_le_add (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin k → U)
    (h : (Fin n → U) → Fin l → U) :
    ecomplexityGiven I f h ≤ ecomplexityGiven I g h + ecomplexityGiven I f g
```

`Cslib.Circuits.ecomplexityGiven_append_le` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L177))

> Knowing more never makes `f` harder: `C(f | g, g') ≤ C(f | g)`.

```lean
theorem ecomplexityGiven_append_le (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin k → U)
    (g' : (Fin n → U) → Fin l → U) :
    ecomplexityGiven I f (fun x => Fin.append (g x) (g' x)) ≤ ecomplexityGiven I f g
```

> ### Over a complete basis

`Cslib.Circuits.ecomplexityGiven_ne_top` (theorem, [line 193](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L193))

```lean
theorem ecomplexityGiven_ne_top [I.IsComplete] (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) : ecomplexityGiven I f g ≠ ⊤
```

`Cslib.Circuits.complexityGiven` (definition, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L199))

> The complexity `C(f | g)` of `f` relative to `g` over a complete basis, as a natural
> number.

```lean
noncomputable def complexityGiven (I : Interpretation σ U) [I.IsComplete]
    (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin k → U) : ℕ
```

`Cslib.Circuits.natCast_complexityGiven` (theorem, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L205))

```lean
theorem natCast_complexityGiven (f : (Fin n → U) → Fin m → U)
(g : (Fin n → U) → Fin k → U) : (complexityGiven I f g : ℕ∞) = ecomplexityGiven I f g
```

`Cslib.Circuits.complexityGiven_self` (theorem, [line 209](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L209))

```lean
theorem complexityGiven_self (f : (Fin n → U) → Fin m → U) :
complexityGiven I f f = 0
```

`Cslib.Circuits.complexityGiven_le_complexity` (theorem, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L215))

```lean
theorem complexityGiven_le_complexity (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) : complexityGiven I f g ≤ complexity I f
```

`Cslib.Circuits.complexity_le_add_complexityGiven` (theorem, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L221))

```lean
theorem complexity_le_add_complexityGiven (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) :
    complexity I f ≤ complexity I g + complexityGiven I f g
```

`Cslib.Circuits.complexity_append_le_add_complexityGiven` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L228))

```lean
theorem complexity_append_le_add_complexityGiven (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) :
    complexity I (fun x => Fin.append (f x) (g x)) ≤ complexity I f + complexityGiven I g f
```

`Cslib.Circuits.complexityGiven_le_add` (theorem, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L235))

```lean
theorem complexityGiven_le_add (f : (Fin n → U) → Fin m → U) (g : (Fin n → U) → Fin k → U)
    (h : (Fin n → U) → Fin l → U) :
    complexityGiven I f h ≤ complexityGiven I g h + complexityGiven I f g
```

`Cslib.Circuits.complexityGiven_append_le` (theorem, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean#L242))

```lean
theorem complexityGiven_append_le (f : (Fin n → U) → Fin m → U)
    (g : (Fin n → U) → Fin k → U) (g' : (Fin n → U) → Fin l → U) :
    complexityGiven I f (fun x => Fin.append (g x) (g' x)) ≤ complexityGiven I f g
```

## Depends on

- [Circuit complexity](complexity.md)

## Sources

- [Cslib/Computability/Circuit/RelativeComplexity.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/RelativeComplexity.lean)
