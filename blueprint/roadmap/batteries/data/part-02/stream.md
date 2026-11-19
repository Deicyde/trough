---
catalog: module
lean: Std.Stream.drop, Std.Stream.take, Std.Stream.fst_take_zero, Std.Stream.fst_take_succ, Std.Stream.snd_take_eq_drop, Std.Stream.takeTR, Std.Stream.fst_takeTR_loop, Std.Stream.fst_takeTR, Std.Stream.snd_takeTR_loop, Std.Stream.snd_takeTR, Std.Stream.take_eq_takeTR, Std.List.stream_drop_eq_drop, Std.List.stream_take_eq_take_drop
statement: formalized
proof: formalized
---

# Stream

`Batteries.Data.Stream`, in [Batteries/Data/Stream.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean), by François G. Dorais.

`Std.Stream.drop` (definition, [line 13](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L13))

> Drop up to `n` values from the stream `s`.

```lean
def drop [Stream σ α] (s : σ) : Nat → σ
```

`Std.Stream.take` (definition, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L21))

> Read up to `n` values from the stream `s` as a list from first to last.

```lean
def take [Stream σ α] (s : σ) : Nat → List α × σ
```

`Std.Stream.fst_take_zero` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L30))

```lean
theorem fst_take_zero [Stream σ α] (s : σ) :
    (take s 0).fst = []
```

`Std.Stream.fst_take_succ` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L33))

```lean
theorem fst_take_succ [Stream σ α] (s : σ) :
    (take s (n+1)).fst = match next? s with
      | none => []
      | some (a, s) => a :: (take s n).fst
```

`Std.Stream.snd_take_eq_drop` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L39))

```lean
theorem snd_take_eq_drop [Stream σ α] (s : σ) (n : Nat) :
    (take s n).snd = drop s n
```

`Std.Stream.takeTR` (definition, [line 48](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L48))

> Tail recursive version of `Stream.take`.

```lean
def takeTR [Stream σ α] (s : σ) (n : Nat) : List α × σ
```

`Std.Stream.fst_takeTR_loop` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L58))

```lean
theorem fst_takeTR_loop [Stream σ α] (s : σ) (acc : List α) (n : Nat) :
    (takeTR.loop s acc n).fst = acc.reverseAux (take s n).fst
```

`Std.Stream.fst_takeTR` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L64))

```lean
theorem fst_takeTR [Stream σ α] (s : σ) (n : Nat) : (takeTR s n).fst = (take s n).fst
```

`Std.Stream.snd_takeTR_loop` (theorem, [line 67](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L67))

```lean
theorem snd_takeTR_loop [Stream σ α] (s : σ) (acc : List α) (n : Nat) :
    (takeTR.loop s acc n).snd = drop s n
```

`Std.Stream.snd_takeTR` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L73))

```lean
theorem snd_takeTR [Stream σ α] (s : σ) (n : Nat) :
    (takeTR s n).snd = drop s n
```

`Std.Stream.take_eq_takeTR` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L76))

```lean
theorem take_eq_takeTR : @take = @takeTR
```

`Std.List.stream_drop_eq_drop` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L81))

```lean
theorem List.stream_drop_eq_drop (l : List α) : Stream.drop l n = l.drop n
```

`Std.List.stream_take_eq_take_drop` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean#L89))

```lean
theorem List.stream_take_eq_take_drop (l : List α) :
    Stream.take l n = (l.take n, l.drop n)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Stream.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Stream.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.Stream.json)
