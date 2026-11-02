---
declaration: theorem
origin: cited
---

# Free 854 magma

The magma $M_{X,854}$ is a free 854 magma on $X$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $f: X \to M$ be a function from $X$ to an $854$ magma $M$, then $\varphi_f$ is a homomorphism from $M_X$ (with the operation $*$) to $M$. We claim that the restriction of $\varphi_f$ to $M_{X,854}$ is a homomorphism from $M_{X,854}$ (with operation $\diamond$) to $M$. Since $\varphi_f$ was already a homomorphism for $*$, it suffices to show that $\varphi_f$ preserves $\to$: that is to say, for any $x,y \in M_{X,854}$, that $x \to y$ implies $\varphi_f(x) \to \varphi_f(y)$. By definition, one of the five scenarios (i)-(v) in [Relation on the free group](free-relate.md) holds, and in each case one can establish the claim from the corresponding claim of [The 854 relation](854-relation.md) and an induction on the max-length of the claim $x \to y$.

It remains to show that $M_{854}$ actually satisfies 854, that is to say that

$$
(y \diamond z) \diamond (x \diamond z) \to x
$$

for all $x,y,z \in M_{854}$. Writing $w = y \diamond z$, we have $z \to w$ by [Relation on the free group](free-relate.md)(i), and we need to show that $w \diamond (x \diamond z) \to x$. We divide into four cases.

Case 1: $x \diamond z \to w$, $z \to x$. Here we have $x \diamond z = x$ and $w \diamond (x \diamond z) = w$. We now have $z \to x,w$ and $x \to w$, and we need to show that $w \to x$.

From one we know that one of

$$
z = x_R, z = x_{RL}, x = z_R, x = z_{RL}
$$

holds, one of

$$
z = w_R, z = w_{RL}, w = z_R, w = z_{RL}
$$

holds, and one of

$$
x = w_R, x = w_{RL}, w = x_R, w = x_{RL}
$$

holds.

We split into subcases using (one-3).

- If $x = w_R$ then the claim follows from [Relation on the free group](free-relate.md)(i).
- If $w = x_{RL}$ then from [Relation on the free group](free-relate.md)(iii) we have $x_{RR} \to x_L$, and then the claim follows from [Relation on the free group](free-relate.md)(ii).
- If $x = w_{RL}$, then $w_{RR} \to w_L$ by [Relation on the free group](free-relate.md)(ii) and from [Relation on the free group](free-relate.md)(iii) we will be done if we can show that $w_R \to w_{RL}$. If $z = w_R$ then this follows from $z \to x$. The claim $z = w_{RL}$ is not compatible with (one-1), since $z=x$ in that case. If $w = z_R$ then $x = z_{RRL}$, and this is only compatible with (one-1) if $x = z_{RL}$, thus $z = a * (x * (x * b))$ and $w = x * (x * b)$ for some $a,b$. In order to have $x = w_{RL}$ in (one-3), we must have $b \to x$ by [Relation on the free group](free-relate.md)(iii), but then $x*b$ would not lie in $M_{854}$, a contradiction.
- If $w = x_R$, then we cannot then have $z = x_R$ as then $z=w$ which is incompatible with (one-2). If $z = x_{RL} = w_L$ then $x_{RR} \to x_L$ by [Relation on the free group](free-relate.md)(ii), and the only available options from (one-2) are $z = w_R$ and $z = w_{RL}$. For $z=w_R$ we have $w = z * z$ and $x = a * (z * z)$ for some $a$ with $z \to a = x_L$. Since $z \to z*z = x_R$ as well by [Relation on the free group](free-relate.md)(i), and $z = x_{RR}$, we obtain $w \to x$ as required from [Relation on the free group](free-relate.md)(iv).

Case 2: $x \diamond z \to w$, $z \not \to x$. We now have $x * z, z \to w$, and we need to show that $w \to x$. From one we know that one of

$$
w = (x * z)_R, w = (x * z)_{RL}, x * z = w_R, x * z = w_{RL}
$$

holds, and that one of

$$
w =  z_R, w = z_{RL}, z = w_R, z = w_{RL}
$$

holds.

We split into cases depending on (wz-1).

- If $w = (x*z)_R$ then $w=z$, which is incompatible with (wz).
- If $w = (x*z)_{RL}$ then $w = z_L$ and $z_R \to x$ by [Relation on the free group](free-relate.md)(ii). Only the first two possibilities of (wz) are compatible with $w=z_L$. In the first case we are done since $z_R \to x$ and $w = z_R$. In the second case, we have $z = w * (w * a)$ for some $a$ with $a \to w$ (from [Relation on the free group](free-relate.md)(ii) and $z \to w$), but then $w * a$ will not lie in $M_{854}$, contradiction.
- If $x*z = w_R$ then $w$ is longer than $z$ and $z \neq w_R$. Comparing this with (wz) we see that the only compatible option is $z = w_{RL}$, thus $x=z$, and then $w = a * (x * x)$ and $x \to a$ by [Relation on the free group](free-relate.md)(iii), and the claim follows from [Relation on the free group](free-relate.md)(ii).
- If $x * z = w_{RL}$, then $w = a * ((x *z) * b)$ for some $a,b$. Then $w$, $w_R$, and $w_{RL}$ are all longer than $z$ and none of the options in (wz) can hold, a contradiction.

Case 3: $x \diamond z \not \to w$, $z \to x$. We now have $z \to x, w$, and we need to show that $w * x \to x$.

If $z \in \{ w_R, w_{RL}, x_R, x_{RL} \}$, then the claim follows from [Relation on the free group](free-relate.md)(iv), so we may assume that this is not the case. By one, we then know that one of

$$
x = z_R, x = z_{RL}
$$

holds, and also one of

$$
w =  z_R, w = z_{RL}
$$

holds. Thus, we either have one of

$$
w = x, w = x_L, x = w_L.
$$

But in any of these three cases the claim follows from [Relation on the free group](free-relate.md)(v).

Case 4: $x \diamond z \not \to w$, $z \not \to x$. Then $x = (w \diamond (x \diamond z))_{RL}$ and $z \to w$, so the claim follows from [Relation on the free group](free-relate.md)(ii).

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 310](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L310)
