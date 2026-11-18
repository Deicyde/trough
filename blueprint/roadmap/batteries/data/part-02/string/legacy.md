---
catalog: module
lean: String.Legacy.mapAux, String.Legacy.map, String.Legacy.drop, String.Legacy.take, String.Legacy.takeWhile, String.Legacy.dropWhile, String.Legacy.foldlAux, String.Legacy.foldl, String.Legacy.front, String.Legacy.back, String.Legacy.posOfAux, String.Legacy.posOf, String.Legacy.revPosOfAux, String.Legacy.revPosOf, String.Legacy.findAux, String.Legacy.find, String.Legacy.revFindAux, String.Legacy.revFind, String.Legacy.foldrAux, String.Legacy.foldr, String.Legacy.anyAux, String.Legacy.any, String.Legacy.all, String.Legacy.contains, Substring.Raw.Legacy.foldl, Substring.Raw.Legacy.foldr, Substring.Raw.Legacy.any, Substring.Raw.Legacy.all, Substring.Raw.Legacy.contains
statement: formalized
proof: formalized
---

# Legacy implementations of `String` operations

`Batteries.Data.String.Legacy`, in [Batteries/Data/String/Legacy.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean), by Leonardo de Moura, Mario Carneiro.

> This file includes old definitions of `String` functions that were downstreamed from core to prevent
> `Batteries.Data.String.Lemmas` from breaking.

`String.Legacy.mapAux` (definition, [line 75](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L75))

> Implementation of `String.Legacy.map`.

```lean
def Legacy.mapAux (f : Char → Char) (i : Pos.Raw) (s : String) : String
```

`String.Legacy.map` (definition, [line 96](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L96))

> Applies the function `f` to every character in a string, returning a string that contains the
> resulting characters.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.map`.
>
> Examples:
>  * `"abc123".map Char.toUpper = "ABC123"`
>  * `"".map Char.toUpper = ""`

```lean
def Legacy.map (f : Char → Char) (s : String) : String
```

`String.Legacy.drop` (definition, [line 113](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L113))

> Removes the specified number of characters (Unicode code points) from the start of the string.
>
> If `n` is greater than `s.length`, returns `""`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.drop`.
>
> Examples:
>  * `"red green blue".drop 4 = "green blue"`
>  * `"red green blue".drop 10 = "blue"`
>  * `"red green blue".drop 50 = ""`

```lean
def Legacy.drop (s : String) (n : Nat) : String
```

`String.Legacy.take` (definition, [line 131](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L131))

> Creates a new string that contains the first `n` characters (Unicode code points) of `s`.
>
> If `n` is greater than `s.length`, returns `s`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.take`.
>
> Examples:
> * `"red green blue".take 3 = "red"`
> * `"red green blue".take 1 = "r"`
> * `"red green blue".take 0 = ""`
> * `"red green blue".take 100 = "red green blue"`

```lean
def Legacy.take (s : String) (n : Nat) : String
```

`String.Legacy.takeWhile` (definition, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L148))

> Creates a new string that contains the longest prefix of `s` in which `p` returns `true` for all
> characters.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.takeWhile`.
>
> Examples:
> * `"red green blue".takeWhile (·.isLetter) = "red"`
> * `"red green blue".takeWhile (· == 'r') = "r"`
> * `"red green blue".takeWhile (· != 'n') = "red gree"`
> * `"red green blue".takeWhile (fun _ => true) = "red green blue"`

```lean
def Legacy.takeWhile (s : String) (p : Char → Bool) : String
```

`String.Legacy.dropWhile` (definition, [line 165](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L165))

> Creates a new string by removing the longest prefix from `s` in which `p` returns `true` for all
> characters.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.dropWhile`.
>
> Examples:
> * `"red green blue".dropWhile (·.isLetter) = " green blue"`
> * `"red green blue".dropWhile (· == 'r') = "ed green blue"`
> * `"red green blue".dropWhile (· != 'n') = "n blue"`
> * `"red green blue".dropWhile (fun _ => true) = ""`

```lean
def Legacy.dropWhile (s : String) (p : Char → Bool) : String
```

`String.Legacy.foldlAux` (definition, [line 175](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L175))

> Auxiliary definition for `String.Legacy.foldl`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.foldlAux`.

```lean
def Legacy.foldlAux {α : Type u} (f : α → Char → α) (s : String) (stopPos : Pos.Raw)
    (i : Pos.Raw) (a : α) : α
```

`String.Legacy.foldl` (definition, [line 196](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L196))

> Folds a function over a string from the left, accumulating a value starting with `init`. The
> accumulated value is combined with each character in order, using `f`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.foldl`.
>
> Examples:
>  * `"coffee tea water".foldl (fun n c => if c.isWhitespace then n + 1 else n) 0 = 2`
>  * `"coffee tea and water".foldl (fun n c => if c.isWhitespace then n + 1 else n) 0 = 3`
>  * `"coffee tea water".foldl (·.push ·) "" = "coffee tea water"`

```lean
def Legacy.foldl {α : Type u} (f : α → Char → α) (init : α) (s : String) : α
```

`String.Legacy.front` (definition, [line 210](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L210))

> Returns the first character in `s`. If `s = ""`, returns `(default : Char)`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.front`.
>
> Examples:
> * `"abc".front = 'a'`
> * `"".front = (default : Char)`

```lean
def Legacy.front (s : String) : Char
```

`String.Legacy.back` (definition, [line 224](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L224))

> Returns the last character in `s`. If `s = ""`, returns `(default : Char)`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `String.back`.
>
> Examples:
> * `"abc".back = 'c'`
> * `"".back = (default : Char)`

```lean
def Legacy.back (s : String) : Char
```

`String.Legacy.posOfAux` (definition, [line 234](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L234))

> Auxuliary definition for `String.Legacy.posOf`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.posOfAux (s : String) (c : Char) (stopPos : Pos.Raw) (pos : Pos.Raw) : Pos.Raw
```

`String.Legacy.posOf` (definition, [line 256](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L256))

> Returns the position of the first occurrence of a character, `c`, in a string `s`. If `s` does not
> contain `c`, returns `s.rawEndPos`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
> * `"abcba".posOf 'a' = ⟨0⟩`
> * `"abcba".posOf 'z' = ⟨5⟩`
> * `"L∃∀N".posOf '∀' = ⟨4⟩`

```lean
def Legacy.posOf (s : String) (c : Char) : Pos.Raw
```

`String.Legacy.revPosOfAux` (definition, [line 266](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L266))

> Auxuliary definition for `String.Legacy.revPosOf`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.revPosOfAux (s : String) (c : Char) (pos : Pos.Raw) : Option Pos.Raw
```

`String.Legacy.revPosOf` (definition, [line 288](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L288))

> Returns the position of the last occurrence of a character, `c`, in a string `s`. If `s` does not
> contain `c`, returns `none`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
> * `"abcabc".revPosOf 'a' = some ⟨3⟩`
> * `"abcabc".revPosOf 'z' = none`
> * `"L∃∀N".revPosOf '∀' = some ⟨4⟩`

```lean
def Legacy.revPosOf (s : String) (c : Char) : Option Pos.Raw
```

`String.Legacy.findAux` (definition, [line 298](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L298))

> Auxuliary definition for `String.Legacy.find`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.findAux (s : String) (p : Char → Bool) (stopPos : Pos.Raw) (pos : Pos.Raw) : Pos.Raw
```

`String.Legacy.find` (definition, [line 321](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L321))

> Finds the position of the first character in a string for which the Boolean predicate `p` returns
> `true`. If there is no such character in the string, then the end position of the string is
> returned.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
>  * `"coffee tea water".find (·.isWhitespace) = ⟨6⟩`
>  * `"tea".find (· == 'X') = ⟨3⟩`
>  * `"".find (· == 'X') = ⟨0⟩`

```lean
def Legacy.find (s : String) (p : Char → Bool) : Pos.Raw
```

`String.Legacy.revFindAux` (definition, [line 331](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L331))

> Auxuliary definition for `String.Legacy.revFind`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.revFindAux (s : String) (p : Char → Bool) (pos : Pos.Raw) : Option Pos.Raw
```

`String.Legacy.revFind` (definition, [line 353](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L353))

> Finds the position of the last character in a string for which the Boolean predicate `p` returns
> `true`. If there is no such character in the string, then `none` is returned.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
>  * `"coffee tea water".revFind (·.isWhitespace) = some ⟨10⟩`
>  * `"tea".revFind (· == 'X') = none`
>  * `"".revFind (· == 'X') = none`

```lean
def Legacy.revFind (s : String) (p : Char → Bool) : Option Pos.Raw
```

`String.Legacy.foldrAux` (definition, [line 363](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L363))

> Auxuliary definition for `String.Legacy.foldr`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.foldrAux {α : Type u} (f : Char → α → α) (a : α) (s : String)
    (i begPos : Pos.Raw) : α
```

`String.Legacy.foldr` (definition, [line 387](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L387))

> Folds a function over a string from the right, accumulating a value starting with `init`. The
> accumulated value is combined with each character in reverse order, using `f`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
>  * `"coffee tea water".foldr (fun c n => if c.isWhitespace then n + 1 else n) 0 = 2`
>  * `"coffee tea and water".foldr (fun c n => if c.isWhitespace then n + 1 else n) 0 = 3`
>  * `"coffee tea water".foldr (fun c s => c.push s) "" = "retaw dna aet eeffoc"`

```lean
def Legacy.foldr {α : Type u} (f : Char → α → α) (init : α) (s : String) : α
```

`String.Legacy.anyAux` (definition, [line 397](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L397))

> Auxuliary definition for `String.Legacy.any`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.anyAux (s : String) (stopPos : Pos.Raw) (p : Char → Bool) (i : Pos.Raw) :
    Bool
```

`String.Legacy.any` (definition, [line 422](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L422))

> Checks whether there is a character in a string for which the Boolean predicate `p` returns `true`.
>
> Short-circuits at the first character for which `p` returns `true`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
>  * `"brown".any (·.isLetter) = true`
>  * `"brown".any (·.isWhitespace) = false`
>  * `"brown and orange".any (·.isLetter) = true`
>  * `"".any (fun _ => false) = false`

```lean
def Legacy.any (s : String) (p : Char → Bool) : Bool
```

`String.Legacy.all` (definition, [line 439](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L439))

> Checks whether the Boolean predicate `p` returns `true` for every character in a string.
>
> Short-circuits at the first character for which `p` returns `false`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
>  * `"brown".all (·.isLetter) = true`
>  * `"brown and orange".all (·.isLetter) = false`
>  * `"".all (fun _ => false) = true`

```lean
def Legacy.all (s : String) (p : Char → Bool) : Bool
```

`String.Legacy.contains` (definition, [line 454](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L454))

> Checks whether a string contains the specified character.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.
>
> Examples:
> * `"green".contains 'e' = true`
> * `"green".contains 'x' = false`
> * `"".contains 'x' = false`

```lean
def Legacy.contains (s : String) (c : Char) : Bool
```

`Substring.Raw.Legacy.foldl` (definition, [line 469](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L469))

> Folds a function over a substring from the left, accumulating a value starting with `init`. The
> accumulated value is combined with each character in order, using `f`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`. Its runtime behavior is equivalent to that of `Substring.Raw.foldl`.

```lean
def Legacy.foldl {α : Type u} (f : α → Char → α) (init : α) (s : Substring.Raw) : α
```

`Substring.Raw.Legacy.foldr` (definition, [line 481](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L481))

> Folds a function over a substring from the right, accumulating a value starting with `init`. The
> accumulated value is combined with each character in reverse order, using `f`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.foldr {α : Type u} (f : Char → α → α) (init : α) (s : Substring.Raw) : α
```

`Substring.Raw.Legacy.any` (definition, [line 494](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L494))

> Checks whether the Boolean predicate `p` returns `true` for any character in a substring.
>
> Short-circuits at the first character for which `p` returns `true`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.any (s : Substring.Raw) (p : Char → Bool) : Bool
```

`Substring.Raw.Legacy.all` (definition, [line 507](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L507))

> Checks whether the Boolean predicate `p` returns `true` for every character in a substring.
>
> Short-circuits at the first character for which `p` returns `false`.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.all (s : Substring.Raw) (p : Char → Bool) : Bool
```

`Substring.Raw.Legacy.contains` (definition, [line 517](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean#L517))

> Checks whether a substring contains the specified character.
>
> This is an old implementation, preserved here for users of the lemmas in
> `Batteries.Data.String.Lemmas`.

```lean
def Legacy.contains (s : Substring.Raw) (c : Char) : Bool
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/String/Legacy.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/String/Legacy.lean)
