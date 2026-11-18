---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.indexExprIsNum, TensorSpecies.Tensor.indexExprIsJiggle, TensorSpecies.Tensor.indexRemoveTau, TensorSpecies.Tensor.indexExprIsBracketEval, TensorSpecies.Tensor.indexToNum, TensorSpecies.Tensor.indexToIdent, TensorSpecies.Tensor.indexToBracketTerm, TensorSpecies.Tensor.indexPosEq
statement: formalized
proof: formalized
---

# Elaboration of tensor expressions

The module `Physlib.Relativity.Tensors.Elab`, [Physlib/Relativity/Tensors/Elab.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean): 37 declarations, 37 with a docstring.

> - Syntax in Lean allows us to represent tensor expressions in a way close to what we expect to
>   see on pen-and-paper.
> - The elaborator turns this syntax into a tensor tree.

## Examples

> - Suppose `T` and `T'` are tensors with color `![c1, c2]`.
> - `{T | μ ν}ᵀ` is `tensorNode T`.
> - We can also write e.g. `{T | μ ν}ᵀ.tensor` to get the tensor itself.
> - `{- T | μ ν}ᵀ` is `neg (tensorNode T)`.
> - `{T | 0 ν}ᵀ` is `eval 0 0 (tensorNode T)`.
> - `{T | [μ] ν}ᵀ` is `eval 0 μ (tensorNode T)`.
> - `{T | μ ν + T' | μ ν}ᵀ` is `addNode (tensorNode T) (perm _ (tensorNode T'))`, where
>   here `_` will be the identity permutation so does nothing.
> - `{T | μ ν = T' | μ ν}ᵀ` is `(tensorNode T).tensor = (perm _ (tensorNode T')).tensor`.
> - If `a ∈ k` then `{a •ₜ T | μ ν}ᵀ` is `smulNode a (tensorNode T)`.
> - If `g ∈ S.G` then `{g •ₐ T | μ ν}ᵀ` is `actionNode g (tensorNode T)`.
> - Suppose `T2` is a tensor with color `![c3]`.
>   Then `{T | μ ν ⊗ T2 | σ}ᵀ` is `prodNode (tensorNode T) (tensorNode T2)`.
> - If `T3` is a tensor with color `![S.τ c1, S.τ c2]`, then
>   `{T | μ ν ⊗ T3 | μ σ}ᵀ` is `contr 0 1 _ (prodNode (tensorNode T) (tensorNode T3))`.
>   `{T | μ ν ⊗ T3 | μ ν }ᵀ` is
>   `contr 0 0 _ (contr 0 1 _ (prodNode (tensorNode T) (tensorNode T3)))`.
> - If `T4` is a tensor with color `![c2, c1]` then
>   `{T | μ ν + T4 | ν μ }ᵀ`is `addNode (tensorNode T) (perm _ (tensorNode T4))` where `_`
>   is the permutation of the two indices of `T4`.
>   `{T | μ ν = T4 | ν μ }ᵀ` is `(tensorNode T).tensor = (perm _ (tensorNode T4)).tensor` is the
>   permutation of the two indices of `T4`.

## Comments

> - In all of these expressions `μ`, `ν` etc are free. It does not matter what they are called,
>   Lean will elaborate them in the same way. In other words, `{T | μ ν ⊗ T3 | μ ν }ᵀ` is exactly
>   the same to Lean as `{T | α β ⊗ T3 | α β }ᵀ`.
> - Note that compared to ordinary index notation, we do not rise or lower the indices.
>   This is for two reasons: 1) It is difficult to make this general for all tensor species,
>   2) It is a redundancy in ordinary index notation, since the tensor `T` itself already tells you
>   this information.

## Indices

**`TensorSpecies.Tensor.indexExprIsNum`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L86).

> Bool which is true if an index is a num.

```lean
def indexExprIsNum (stx : Syntax) : Bool
```

**`TensorSpecies.Tensor.indexExprIsJiggle`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L92).

> Bool which is true if an index is a jiggle `τ(i)`.

```lean
def indexExprIsJiggle (stx : Syntax) : Bool
```

**`TensorSpecies.Tensor.indexRemoveTau`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L99).

> Removes a `τ(⬝)` wrapper from an index, leaving any other index unchanged. Pure, so it can be
> used to compare indices up to `τ` (e.g. when counting contractions in `withoutContrEval`).

```lean
def indexRemoveTau (stx : TSyntax `indexExpr) : TSyntax `indexExpr
```

**`TensorSpecies.Tensor.indexExprIsBracketEval`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L105).

> Bool which is true if an index is evaluated bracket `[μ]`.

```lean
def indexExprIsBracketEval(stx : Syntax) : Bool
```

**`TensorSpecies.Tensor.indexToNum`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L111).

> If an index is a num - the underlying natural number.

```lean
def indexToNum (stx : Syntax) : TermElabM Nat
```

**`TensorSpecies.Tensor.indexToIdent`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L121).

> When an index is not a num, the corresponding ident.

```lean
def indexToIdent (stx : Syntax) : TermElabM Ident
```

**`TensorSpecies.Tensor.indexToBracketTerm`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L129).

> For an evaluated bracket index `[t]`, the term `t` giving the value of the index.

```lean
def indexToBracketTerm (stx : Syntax) : TermElabM Term
```

**`TensorSpecies.Tensor.indexPosEq`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L137).

> Takes a pair ``a b : ℕ × TSyntax `indexExpr``. If `a.1 < b.1` and `a.2 = b.2` then
> outputs `some (a.1, b.1)`, otherwise `none`.

```lean
def indexPosEq (a b : TSyntax `indexExpr × ℕ) : TermElabM (Option (ℕ × ℕ))
```

**`TensorSpecies.Tensor.indexToDual`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L146).

> Bool which is true if an index is of the form τ(i) that is, to be dualed.

```lean
def indexToDual (stx : Syntax) : Bool
```

## Manipulation of lists of indexExpr

**`TensorSpecies.Tensor.evalAdjustPos`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L162).

> Adjusts a list `List ℕ` by subtracting from each natural number the number
> of elements before it in the list which are less than itself. This is used
> to form a list of pairs which can be used for evaluating indices.

```lean
def evalAdjustPos (l : List ℕ) : List ℕ
```

**`TensorSpecies.Tensor.getJigglePos`**, a def, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L172).

> Returns the positions of indices which are "jiggled", i.e., of the form `τ(μ)`,
> these are the indices which are to be raised or lowered.

```lean
def getJigglePos (ind : List (TSyntax `indexExpr)) : TermElabM (List ℕ)
```

**`TensorSpecies.Tensor.getEvalPos`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L192).

> For list of `indexExpr` e.g. `[α, 3, β, 2, γ]`, `getEvalPos`
> returns a list of pairs `ℕ × ℕ` related to indices which are numbers.
> The second element of each pair is the number corresponding to that index.
> The first element is the position of that number in the list of indices when
> all other numbered indices before it are removed. Thus for the example given
> `getEvalPos` outputs `[(1, 3), (2, 2)]`.

```lean
def getEvalPos (ind : List (TSyntax `indexExpr)) : TermElabM (List (ℕ × ℕ))
```

**`TensorSpecies.Tensor.getEvalBracketPos`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L206).

> For list of `indexExpr` e.g. `[α, 3, β, 2, [γ]]`, `getEvalPos`
> returns a list of pairs `ℕ × Term` related to indices which are evaluated
> e.g. `[μ]`.
> The second element of each pair is the value corresponding to that index.
> The first element is the position of that number in the list of indices when
> all other numbered indices before it are removed. Thus for the example given
> `getEvalBracketPos` outputs `[(4, γ)]`.

```lean
def getEvalBracketPos (ind : List (TSyntax `indexExpr)) : TermElabM (List (ℕ × Term))
```

**`TensorSpecies.Tensor.getContrPos`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L218).

> For list of `indexExpr` e.g. `[α, 3, β, α, 2, γ]`, `getContrPos`
> first removes all indices which are numbers (e.g. `[α, β, α, γ]`).
> It then outputs pairs `(a, b)` in `ℕ × ℕ` of positions of this list with `a < b`
> such that the index at `a` is equal to the index at `b`. It checks whether or not
> an element is contracted more then once.

```lean
def getContrPos (ind : List (TSyntax `indexExpr)) : TermElabM (List (ℕ × ℕ))
```

**`TensorSpecies.Tensor.withoutContrEval`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L236).

> The list of indices after contraction or evaluation.

```lean
def withoutContrEval (ind : List (TSyntax `indexExpr)) : TermElabM (List (TSyntax `indexExpr))
```

**`TensorSpecies.Tensor.toPairs`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L256).

> Takes a list and puts consecutive elements into pairs.
> e.g. [0, 1, 2, 3] becomes [(0, 1), (2, 3)].

```lean
def toPairs (l : List ℕ) : List (ℕ × ℕ)
```

**`TensorSpecies.Tensor.contrListAdjust`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L265).

> Adjusts a list `List (ℕ × ℕ)` by subtracting from each natural number the number
> of elements before it in the list which are less than itself. This is used
> to form a list of pairs which can be used for contracting indices.

```lean
def contrListAdjust (l : List (ℕ × ℕ)) : List (ℕ × ℕ)
```

## Permutations of indices

**`TensorSpecies.Tensor.getPermutation`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L280).

> Given two lists of indices, all of which are identifiers, returns the `List (ℕ)` whose
> `i`th entry is the position in `l2` of the `i`th index in `l1`.

```lean
def getPermutation (l1 l2 : List (TSyntax `indexExpr)) : TermElabM (List ℕ)
```

**`TensorSpecies.Tensor.stringToTerm`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L292).

> The construction of an expression corresponding to the type of a given string once parsed.

```lean
def stringToTerm (str : String) : TermElabM Term
```

## Syntax for tensor expressions.

## Syntax of tensor expressions to indices.

**`TensorSpecies.Tensor.getNumIndicesExact`**, a def, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L343).

> For syntax of the form `T` where `T` is `Tensor S c` this returns
> the value of `TensorSpecies.numIndices T`. That is, the exact number of indices
> associated with that tensor.

```lean
def getNumIndicesExact (stx : Syntax) : TermElabM ℕ
```

**`TensorSpecies.Tensor.getAllIndices`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L356).

> For syntax of the form `T | α β 2 β `, `getAllIndices` returns a list `[α, β, 2, β]`
> of all `indexExpr`.

```lean
def getAllIndices (stx : Syntax) : TermElabM (List (TSyntax `indexExpr))
```

## Modifying terms to tensor trees

**`TensorSpecies.Tensor.TensorExpressionOperator`**, an abbrev, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L388).

> A Tensor expression operator is a map which takes in a pair
> consisting of a list of indices and a term and outputs a list of indices and a term,
> after applying a certain operation.

```lean
abbrev TensorExpressionOperator
```

**`TensorSpecies.Tensor.TensorExpressionOperator.create`**, a def, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L392).

> The creation of a tensor from a syntax tree.

```lean
def TensorExpressionOperator.create (stx : Syntax) :
    TermElabM (List (TSyntax `indexExpr) × Term)
```

**`TensorSpecies.Tensor.TensorExpressionOperator.jiggle`**, a def, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L407).

> The tensor expression operator which rises or lowers the indices of a tensor based on
> indices with `τ`-syntax.

```lean
def TensorExpressionOperator.jiggle : TensorExpressionOperator
```

**`TensorSpecies.Tensor.TensorExpressionOperator.eval`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L415).

> The tensor expression operator which evaluates indices.

```lean
def TensorExpressionOperator.eval : TensorExpressionOperator
```

**`TensorSpecies.Tensor.TensorExpressionOperator.contr`**, a def, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L429).

> The tensor expression operator which contracts indices.

```lean
def TensorExpressionOperator.contr : TensorExpressionOperator
```

**`TensorSpecies.Tensor.TensorExpressionOperator.prod`**, a def, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L441).

> The tensor expression operator which takes the product of two tensors.

```lean
def TensorExpressionOperator.prod : List (TSyntax `indexExpr) × Term →
    List (TSyntax `indexExpr) × Term →
    TermElabM (List (TSyntax `indexExpr) × Term)
```

**`TensorSpecies.Tensor.TensorExpressionOperator.neg`**, a def, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L449).

> The tensor expression operator which negates a tensor.

```lean
def TensorExpressionOperator.neg : TensorExpressionOperator
```

**`TensorSpecies.Tensor.TensorExpressionOperator.smul`**, a def, [line 454](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L454).

> The tensor expression operator which multiplies a tensor by a scalar.

```lean
def TensorExpressionOperator.smul (c : Term) : TensorExpressionOperator
```

**`TensorSpecies.Tensor.TensorExpressionOperator.action`**, a def, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L459).

> The tensor expression operator which acts on a tensor by a group element.

```lean
def TensorExpressionOperator.action (c : Term) : TensorExpressionOperator
```

**`TensorSpecies.Tensor.colorsDefEq`**, a def, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L467).

> Whether `T1` and `T2` elaborate to tensors of definitionally equal colour (equal type).
> Used to decide whether an identity reindexing between them may be dropped: the bare,
> un-`permT`'d term is well typed exactly when the two colours agree by `rfl`. The check
> elaborates speculatively and restores the elaborator state afterwards.

```lean
def colorsDefEq (T1 T2 : Term) : TermElabM Bool
```

**`TensorSpecies.Tensor.permWrap`**, a def, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L480).

> Wraps `T` in the reindexing `permT ![lPerm] IsReindexing.auto`.

```lean
def permWrap (lPerm : List ℕ) (T : Term) : TermElabM Term
```

**`TensorSpecies.Tensor.TensorExpressionOperator.add`**, a def, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L486).

> The tensor expression operator which adds two tensors.

```lean
def TensorExpressionOperator.add : List (TSyntax `indexExpr) × Term →
    List (TSyntax `indexExpr) × Term →
    TermElabM (List (TSyntax `indexExpr) × Term)
```

**`TensorSpecies.Tensor.TensorExpressionOperator.equal`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L499).

> The tensor expression operator which equates two tensors.

```lean
def TensorExpressionOperator.equal : List (TSyntax `indexExpr) × Term →
    List (TSyntax `indexExpr) × Term →
    TermElabM (List (TSyntax `indexExpr) × Term)
```

## Syntax to tensor tree

**`TensorSpecies.Tensor.syntaxFull`**, a def, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L519).

> Takes a syntax corresponding to a tensor expression and turns it into a
> term corresponding to a tensor tree.

```lean
partial def syntaxFull (stx : Syntax) : TermElabM (List (TSyntax `indexExpr) × Term)
```

## Elaboration

**`TensorSpecies.Tensor.stripToTensorSelf`**, a def, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L558).

> Removes redundant `Tensorial.toTensor` coercions from an elaborated tensor expression:
> every subterm `Tensorial.toTensor t` whose `Tensorial` instance is the canonical instance
> on `S.Tensor c` (`Tensorial.self`) is replaced by `t` itself, since there the coercion is
> the identity. Coercions coming from genuine tensorial instances (e.g. on Lorentz vectors)
> carry real information and are left untouched.

```lean
def stripToTensorSelf (e : Expr) : Expr
```

**`TensorSpecies.Tensor.elaborateTensorNode`**, a def, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean#L570).

> Takes a syntax corresponding to a tensor expression and turns it into an
> expression corresponding to a tensor tree. The redundant `Tensorial.toTensor` coercions
> inserted for bare `S.Tensor` terms are removed via `stripToTensorSelf`.

```lean
def elaborateTensorNode (stx : Syntax) : TermElabM Expr
```

## Test cases

> We pin the elaboration of the `{ … }ᵀ` notation for each construct it supports: bare tensor
> nodes, a genuine `Tensorial` instance, negation, evaluation, scalar multiplication, the group
> action, products, contractions, addition and equality. Together these check that the elaborator
> inserts neither a redundant `Tensorial.toTensor` wrapper on a bare `S.Tensor` term nor an
> identity `permT` when the two sides already align, while keeping the `toTensor` coercion of a
> genuine `Tensorial` instance and a genuine `permT` for a real reindexing.

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Tensors/Elab.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Elab.lean)
