---
catalog: module
lean: Montgomery.gcdInner_zero, Montgomery.gcdInner_succ, Montgomery.gcdInner_natAbs_le, Montgomery.gcdInner_natAbs_le_31
statement: formalized
proof: formalized
---

# Word-sized divsteps: coefficient bounds

`CompPoly.Fields.Montgomery.Divstep`, in [CompPoly/Fields/Montgomery/Divstep.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Divstep.lean), by Georgios Raikos.

> Unfolding lemmas for `gcdInner` of `Montgomery/DivstepDefs`, and the bound on the entries of
> its transition matrix. A chunk of at most 31 divsteps keeps `|f| + |g| ≤ 2^31` in each row.
> The linear combinations of the multi-limb inversion runtimes require that bound.

`Montgomery.gcdInner_zero` (theorem, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Divstep.lean#L23))

> Unfolding of the empty divstep run.

```lean
theorem gcdInner_zero (a b : UInt64) (f0 g0 f1 g1 : Int) :
    gcdInner 0 a b f0 g0 f1 g1 = (a, b, f0, g0, f1, g1)
```

`Montgomery.gcdInner_succ` (theorem, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Divstep.lean#L27))

> Unfolding of one divstep.

```lean
theorem gcdInner_succ (rounds : Nat) (a b : UInt64) (f0 g0 f1 g1 : Int) :
    gcdInner (rounds + 1) a b f0 g0 f1 g1 =
      if a &&& 1 == 0 then
        gcdInner rounds (a >>> 1) b f0 g0 (f1 * 2) (g1 * 2)
      else if a < b then
        gcdInner rounds ((b - a) >>> 1) a (f1 - f0) (g1 - g0) (f0 * 2) (g0 * 2)
      else
        gcdInner rounds ((a - b) >>> 1) b (f0 - f1) (g0 - g1) (f1 * 2) (g1 * 2)
```

`Montgomery.gcdInner_natAbs_le` (theorem, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Divstep.lean#L44))

> Transition entries at most double per divstep.

```lean
theorem gcdInner_natAbs_le {rounds : Nat} {a b a' b' : UInt64}
    {f0 g0 f1 g1 f0' g0' f1' g1' : Int} {n : Nat}
    (h0 : f0.natAbs + g0.natAbs ≤ n) (h1 : f1.natAbs + g1.natAbs ≤ n)
    (heq : gcdInner rounds a b f0 g0 f1 g1 = (a', b', f0', g0', f1', g1')) :
    f0'.natAbs + g0'.natAbs ≤ 2 ^ rounds * n ∧
      f1'.natAbs + g1'.natAbs ≤ 2 ^ rounds * n
```

`Montgomery.gcdInner_natAbs_le_31` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Divstep.lean#L74))

> Chunks of at most 31 divsteps satisfy the linear-combination bound.

```lean
theorem gcdInner_natAbs_le_31 {rounds : Nat} (h31 : rounds ≤ 31) {a b a' b' : UInt64}
    {f0' g0' f1' g1' : Int}
    (heq : gcdInner rounds a b 1 0 0 1 = (a', b', f0', g0', f1', g1')) :
    f0'.natAbs + g0'.natAbs ≤ 2 ^ 31 ∧ f1'.natAbs + g1'.natAbs ≤ 2 ^ 31
```

## Depends on

- [Word-sized divsteps: runtime definitions (zero-import)](divstepdefs.md)

## Sources

- [CompPoly/Fields/Montgomery/Divstep.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Divstep.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Divstep.json)
