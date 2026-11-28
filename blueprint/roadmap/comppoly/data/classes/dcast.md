---
catalog: module
lean: cast_eq_cast_iff, cast_symm, congrArg₃, congrArg₄, DCast, dcast_eq, dcast_symm, dcast_trans, dcast_eq_dcast_iff, heq_of_dcast, dcast_fun, dcast_fun₂, dcast_eq_root_cast, DCast₂, dcast₂_eq, dcast₂_eq', dcast₂_symm, dcast₂_trans, dcast₂_eq_dcast₂_iff, dcast₂_dcast, instDCast₁₂, instDCastPSigma, instDCastSigma, instDCastForall, DCast₃, dcast₃_eq, dcast₃_symm, dcast₃_trans, dcast₃_eq_dcast₃_iff, dcast₃_dcast₂, instDCast₂₃, instDCast₁₃, instDCast₂PSigma, instDCast₂Sigma, instDCast₂Forall, instDCastPSigmaPSigma, instDCastSigmaSigma, instDCastForallForall, instDCastPSigmaForall, instDCastSigmaForallForall, Fin.instDCast, Fin.cast_eq_dcast
statement: formalized
proof: formalized
---

# Dependent casts

`CompPoly.Data.Classes.DCast`, in [CompPoly/Data/Classes/DCast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean), by Quang Dao.

> This file contains type classes for dependent or custom cast operations
>
> This allows us to state theorems with more refined casts, without which we cannot make progress in
> proving them

`cast_eq_cast_iff` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L26))

```lean
theorem cast_eq_cast_iff {α β γ : Sort u} {h : α = γ} {h' : β = γ} {a : α} {b : β} :
    cast h a = cast h' b ↔ a = cast (h'.trans h.symm) b
```

`cast_symm` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L29))

```lean
theorem cast_symm {α β : Sort u} {h : α = β} {a : α} {b : β} :
    cast h a = b ↔ a = cast h.symm b
```

`congrArg₃` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L33))

```lean
theorem congrArg₃ {α β γ δ : Sort*} {f : α → β → γ → δ} {a a' : α} {b b' : β} {c c' : γ}
    (h : a = a') (h' : b = b') (h'' : c = c') : f a b c = f a' b' c'
```

`congrArg₄` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L37))

```lean
theorem congrArg₄ {α β γ δ ε : Sort*} {f : α → β → γ → δ → ε} {a a' : α} {b b' : β} {c c' : γ}
    {d d' : δ} (h : a = a') (h' : b = b') (h'' : c = c') (h''' : d = d') :
      f a b c d = f a' b' c' d'
```

`DCast` (class, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L48))

> `DCast` is a type class for custom cast operations on an indexed type family `β a`
>
> We require the cast operation `dcast`, along with the property that `dcast` reduces to `id` under
> reflexivity.

```lean
class DCast (α : Sort*) (β : α → Sort*) where
  dcast : ∀ {a a' : α}, a = a' → β a → β a'
  dcast_id : ∀ {a : α}, dcast (Eq.refl a) = id
```

`dcast_eq` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L65))

```lean
theorem dcast_eq : dcast (Eq.refl a) b = b
```

`dcast_symm` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L68))

```lean
theorem dcast_symm (ha : a = a') (hb : dcast ha b = b') : dcast (ha.symm) b' = b
```

`dcast_trans` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L72))

```lean
theorem dcast_trans (h : a = a') (h' : a' = a'') :
    dcast h' (dcast h b) = dcast (h.trans h') b
```

`dcast_eq_dcast_iff` (theorem, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L76))

```lean
theorem dcast_eq_dcast_iff (h : a = a'') (h' : a' = a'') :
    dcast h b = dcast h' b' ↔ b = dcast (h'.trans h.symm) b'
```

`heq_of_dcast` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L80))

```lean
theorem heq_of_dcast (ha : a = a') (hb : dcast ha b = b') : HEq b b'
```

`dcast_fun` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L83))

```lean
theorem dcast_fun {γ : (a : α) → β a → Sort*} {f : (b : β a) → γ a b} :
    f (dcast rfl b) = dcast (α := β a) (β := γ a) dcast_eq.symm (f b)
```

`dcast_fun₂` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L90))

```lean
theorem dcast_fun₂ {a₁ a₂ a₁' a₂' : α} {h₁ : a₁ = a₁'} {h₂ : a₂ = a₂'} {f : α → α → α}
    {g : (a₁ : α) → (a₂ : α) → β a₁ → β a₂ → β (f a₁ a₂)} {b₁ : β a₁} {b₂ : β a₂} :
    dcast (by cases h₁; cases h₂; rfl) (g a₁ a₂ b₁ b₂) = g a₁' a₂' (dcast h₁ b₁) (dcast h₂ b₂)
```

`dcast_eq_root_cast` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L95))

```lean
theorem dcast_eq_root_cast (h : a = a') : dcast h b = _root_.cast (congrArg β h) b
```

`DCast₂` (class, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L105))

> `DCast₂` is a type class for custom cast operations on a doubly-indexed type family `γ a b`,
>   given an underlying dependent cast `DCast α β`
>
> We require the cast operation `dcast₂`, along with the property that `dcast₂` reduces to `id` under
> reflexivity.

```lean
class DCast₂ (α : Sort*) (β : α → Sort*) (γ : (a : α) → β a → Sort*) [DCast α β] where
  dcast₂ : ∀ {a a' : α} {b : β a} {b' : β a'},
    (ha : a = a') → (dcast ha b = b') → γ a b → γ a' b'
  dcast₂_id : ∀ {a : α} {b : β a}, dcast₂ (Eq.refl a) dcast_eq = (id : γ a b → γ a b)
```

`dcast₂_eq` (theorem, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L126))

```lean
theorem dcast₂_eq : dcast₂ (Eq.refl a) dcast_eq c = c
```

`dcast₂_eq'` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L130))

```lean
theorem dcast₂_eq' (h : a = a) (h' : dcast h b = b) : dcast₂ h h' c = c
```

`dcast₂_symm` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L133))

```lean
theorem dcast₂_symm (ha : a = a') (hb : dcast ha b = b') (hc : dcast₂ ha hb c = c') :
    dcast₂ ha.symm (dcast_symm ha hb) c' = c
```

`dcast₂_trans` (theorem, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L138))

```lean
theorem dcast₂_trans (ha : a = a') (ha' : a' = a'')
    (hb : dcast ha b = b') (hb' : dcast ha' b' = b'') :
      dcast₂ ha' hb' (dcast₂ ha hb c) = dcast₂ (ha.trans ha') (by simp [← hb', ← hb]) c
```

`dcast₂_eq_dcast₂_iff` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L143))

```lean
theorem dcast₂_eq_dcast₂_iff (ha : a = a'') (ha' : a' = a'')
    (hb : dcast ha b = b'') (hb' : dcast ha' b' = b'') :
    dcast₂ ha hb c = dcast₂ ha' hb' c' ↔
      c = dcast₂ (ha'.trans ha.symm)
        ((dcast_eq_dcast_iff ha ha').mp (hb.trans hb'.symm)).symm c'
```

`dcast₂_dcast` (theorem, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L150))

```lean
theorem dcast₂_dcast : dcast₂ rfl rfl c = dcast dcast_eq.symm c
```

`instDCast₁₂` (instance, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L153))

```lean
instance instDCast₁₂ : DCast (β a) (γ a)
```

`instDCastPSigma` (instance, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L157))

```lean
instance instDCastPSigma : DCast ((a : α) ×' β a) (fun a => γ a.1 a.2)
```

`instDCastSigma` (instance, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L161))

```lean
instance instDCastSigma {α : Type*} {β : α → Type*} {γ : (a : α) → β a → Type*}
    [DCast α β] [DCast₂ α β γ] : DCast ((a : α) × β a) (fun a => γ a.1 a.2)
```

`instDCastForall` (instance, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L166))

```lean
instance instDCastForall : DCast α (fun a => ∀ b : β a, γ a b)
```

`DCast₃` (class, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L181))

> `DCast₃` is a type class for custom cast operations on a triply-indexed type family `δ a b c`,
>   given underlying dependent casts `DCast α β` and `DCast₂ α β γ`
>
> We require the cast operation `dcast₃`, along with the property that `dcast₃` reduces to `id` under
> reflexivity.

```lean
class DCast₃ (α : Sort*) (β : α → Sort*) (γ : (a : α) → β a → Sort*)
    (δ : (a : α) → (b : β a) → γ a b → Sort*) [DCast α β] [DCast₂ α β γ] where
  dcast₃ : ∀ {a a' : α} {b : β a} {b' : β a'} {c : γ a b} {c' : γ a' b'},
    (ha : a = a') → (hb : dcast ha b = b') → (hc : dcast₂ ha hb c = c') → δ a b c → δ a' b' c'
  dcast₃_id : ∀ {a : α} {b : β a} {c : γ a b},
    dcast₃ (Eq.refl a) dcast_eq dcast₂_eq = (id : δ a b c → δ a b c)
```

`dcast₃_eq` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L208))

```lean
theorem dcast₃_eq : dcast₃ (Eq.refl a) dcast_eq dcast₂_eq d = d
```

`dcast₃_symm` (theorem, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L211))

```lean
theorem dcast₃_symm (ha : a = a') (hb : dcast ha b = b') (hc : dcast₂ ha hb c = c')
    (hd : dcast₃ ha hb hc d = d') :
    dcast₃ ha.symm (dcast_symm ha hb) (dcast₂_symm ha hb hc) d' = d
```

`dcast₃_trans` (theorem, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L217))

```lean
theorem dcast₃_trans (ha : a = a') (ha' : a' = a'')
    (hb : dcast ha b = b') (hb' : dcast ha' b' = b'')
    (hc : dcast₂ ha hb c = c') (hc' : dcast₂ ha' hb' c' = c'') :
    dcast₃ ha' hb' hc' (dcast₃ ha hb hc d) =
    dcast₃ (ha.trans ha') (by simp [← hb', ← hb]) (by simp [← hc', ← hc]) d
```

`dcast₃_eq_dcast₃_iff` (theorem, [line 224](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L224))

```lean
theorem dcast₃_eq_dcast₃_iff (ha : a = a') (hb : dcast ha b = b') (hc : dcast₂ ha hb c = c') :
    dcast₃ ha hb hc d = d' ↔ d = dcast₃ ha.symm (dcast_symm ha hb) (dcast₂_symm ha hb hc) d'
```

`dcast₃_dcast₂` (theorem, [line 228](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L228))

```lean
theorem dcast₃_dcast₂ : dcast₃ rfl rfl rfl d = dcast₂ dcast_eq.symm dcast₂_dcast.symm d
```

`instDCast₂₃` (instance, [line 231](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L231))

```lean
instance instDCast₂₃ {a : α} : DCast₂ (β a) (γ a) (δ a)
```

`instDCast₁₃` (instance, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L235))

```lean
instance instDCast₁₃ {a : α} {b : β a} : DCast (γ a b) (δ a b)
```

`instDCast₂PSigma` (instance, [line 239](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L239))

```lean
instance instDCast₂PSigma : DCast₂ ((a : α) ×' β a) (fun a => γ a.1 a.2) (fun a => δ a.1 a.2)
```

`instDCast₂Sigma` (instance, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L244))

```lean
instance instDCast₂Sigma {α : Type*} {β : α → Type*} {γ : (a : α) → β a → Type*}
    {δ : (a : α) → (b : β a) → γ a b → Type*}
    [DCast α β] [DCast₂ α β γ] [DCast₃ α β γ δ] :
    DCast₂ ((a : α) × β a) (fun a => γ a.1 a.2) (fun a => δ a.1 a.2)
```

`instDCast₂Forall` (instance, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L251))

```lean
instance instDCast₂Forall :
    DCast₂ α (fun a => ∀ b : β a, γ a b) (fun a f => ∀ b : β a, δ a b (f b))
```

`instDCastPSigmaPSigma` (instance, [line 257](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L257))

```lean
instance instDCastPSigmaPSigma :
    DCast ((a : α) ×' (b : β a) ×' γ a b) (fun a => δ a.1 a.2.1 a.2.2)
```

`instDCastSigmaSigma` (instance, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L262))

```lean
instance instDCastSigmaSigma {α : Type*} {β : α → Type*} {γ : (a : α) → β a → Type*}
    {δ : (a : α) → (b : β a) → γ a b → Type*}
    [DCast α β] [DCast₂ α β γ] [DCast₃ α β γ δ] :
    DCast ((a : α) × (b : β a) × γ a b) (fun a => δ a.1 a.2.1 a.2.2)
```

`instDCastForallForall` (instance, [line 269](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L269))

```lean
instance instDCastForallForall :
    DCast α (fun a => ∀ b : β a, ∀ c : γ a b, δ a b c)
```

`instDCastPSigmaForall` (instance, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L275))

```lean
instance instDCastPSigmaForall :
    DCast ((a : α) ×' (β a)) (fun ab => ∀ c : γ ab.1 ab.2, δ ab.1 ab.2 c)
```

`instDCastSigmaForallForall` (instance, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L281))

```lean
instance instDCastSigmaForallForall {α : Type*} {β : α → Type*} {γ : (a : α) → β a → Type*}
    {δ : (a : α) → (b : β a) → γ a b → Type*}
    [DCast α β] [DCast₂ α β γ] [DCast₃ α β γ δ] :
    DCast ((a : α) × (β a)) (fun ab => ∀ c : γ ab.1 ab.2, δ ab.1 ab.2 c)
```

`Fin.instDCast` (instance, [line 294](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L294))

> `Fin.cast` as a `DCast` (which should override the default instance).

```lean
instance instDCast : DCast Nat Fin
```

`Fin.cast_eq_dcast` (theorem, [line 298](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean#L298))

```lean
theorem cast_eq_dcast {m n : ℕ} (h : m = n) (a : Fin m) :
    Fin.cast h a = dcast h a
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Classes/DCast.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Classes/DCast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Classes.DCast.json)
