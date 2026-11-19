# The structural hierarchy

We will now establish the hierarchy of types that our model will be built inside.

- [path](def-path.md)

Many of the objects in this construction have an associated type level $\alpha : \lambda^\bot$, and by application of a path of the form $\alpha \rightsquigarrow \beta$ or $\beta \rightsquigarrow \alpha$, we can often define a new object of type level $\beta$. For this common task, we register the following notation typeclasses.

- $x \Downarrow A$ is the *derivative* of an object of type $\beta$ along a path $A : \beta \rightsquigarrow \gamma$, giving an object of type $\gamma$;
- $x \downarrow h$ abbreviates $x \Downarrow \operatorname{\mathsf{single}}(h)$; (In practice the typeclasses will probably not formally depend on each other, and this ‘abbreviation’ may not be a definitional equality.)
- $x \underset{\bot}{\Downarrow} A$ is the *base derivative* of an object of type $\beta$ along a path $A : \beta \rightsquigarrow \bot$;
- $x \underset{\bot}{\downarrow}$ abbreviates $x \underset{\bot}{\Downarrow} \operatorname{\mathsf{single}}(h)$ where $h$ is the canonical proof of $\bot < \beta$ whenever $\beta : \lambda$;
- $x \Uparrow A$ is the *coderivative* of an object of type $\beta$ along a path $A : \alpha \rightsquigarrow \beta$, giving an object of type $\alpha$;
- $x \uparrow h$ abbreviates $x \Uparrow \operatorname{\mathsf{single}}(h)$.

When we say that an object has an associated type level in this context, we mean that the notation typeclass is registered in the following form.

```
class Derivative (X : Type _) (Y : outParam (Type _))
    (β : outParam TypeIndex) (γ : TypeIndex) where
  deriv : X → Path β γ → Y
```

This means that when inferring the type of the expression $x \Downarrow A$, we first compute the type of $x$, which gives rise to a unique type index $\beta$, then the type of $A$ is inferred to give $\gamma$, then the output type $Y$ is uniquely determined.

The reason that we distinguish $\underset{\bot}{\Downarrow}$ from $\Downarrow$ is that the associated type $Y$ is allowed to differ between the two forms. We will give a brief example motivated by a definition we are about to make. For each type index $\beta$, there is a type of $\beta$-structural permutation, comprised of many base permutations. If we have a path $\beta \rightsquigarrow \gamma$, we can convert a $\beta$-structural permutation into a $\gamma$-structural permutation; this will be the derivative map. We will see that a given $\bot$-structural permutation contains exactly one base permutation, and so the types are in canonical isomorphism. If $x$ is a $\beta$-structural permutation and $A : \beta \rightsquigarrow \bot$, then $x \Downarrow A$ is a $\bot$-structural permutation, and $x \underset{\bot}{\Downarrow} A$ is the corresponding base permutation.

Because $\uparrow, \downarrow$ and others are already used by Lean, we use slightly different notation in practice (e.g. $\nearrow, \searrow$). In this writeup, however, we will use subscripts for derivatives and superscripts for coderivatives. We will not distinguish typographically here between the single- and double-struck variants, or between $\Downarrow$ and $\underset{\bot}{\Downarrow}$; in the latter case, the syntax $x_A$ always means $x \underset{\bot}{\Downarrow} A$ whenever $A$ has minimal element $\bot$. We will also use $x_\gamma$ to denote the derivative $x_h$ where $h$ is some proof of $\gamma < \beta$, and use $x^\alpha$ to denote $x^h$ where $h : \beta < \alpha$.

**Definition (derivatives of paths).** If $A : \alpha \rightsquigarrow \beta$ and $B : \beta \rightsquigarrow \gamma$, the derivative $A_B$ is defined to be the union $A \cup B : \alpha \rightsquigarrow \gamma$, and the coderivative $B^A$ is defined to be $A_B$.

- [tree](def-tree.md)
- [structural permutation](def-strperm.md)

As an implementation detail, we create a typeclass $\texttt{StrPermClass}_\alpha$ for permutations that ‘act like’ $\alpha$-permutations: they have a group structure and a canonical group embedding into $\mathsf{StrPerm}_\alpha$. When we quantify over structural permutations in this paper, it should be formalised using an additional quantification over $\texttt{StrPermClass}_\alpha$.

- [enumeration](def-enumeration.md)
- [base support](def-basesupport.md)
- [structural support](def-strsupport.md)
- [structural set](def-strset.md)
