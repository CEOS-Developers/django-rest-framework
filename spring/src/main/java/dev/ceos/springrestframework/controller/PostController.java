package dev.ceos.springrestframework.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import dev.ceos.springrestframework.model.Post;
import dev.ceos.springrestframework.model.PostRepository;

@RestController
@RequestMapping("/api/v1")
public class PostController {

    @Autowired
    private PostRepository postRepository;

    // localhost:8080/api/v1/posts?text=안녕나야&likeCount=123
    @GetMapping("/posts")
    public String getPosts(@RequestParam String text,
                           @RequestParam String likeCount) {

        Post post = new Post(text, Integer.valueOf(likeCount));
        Post savedPost = postRepository.save(post);

        return savedPost.toString();
    }


    @GetMapping("/response")
    public ResponseEntity response() {
        Post post = postRepository.findById(1L)
                .orElseThrow(() -> new IllegalArgumentException("없음"));
        return ResponseEntity.ok(new ResponseExample(post.getText(), post.getLikesCount()).toString());
    }//잭슨 문제

    @PostMapping("/posts")
    public String postPosts(@RequestBody String text,
                            @RequestBody String likeCount) {

        Post post = new Post(text, Integer.valueOf(likeCount));
        Post savedPost = postRepository.save(post);

        return savedPost.toString();
    }


/*
    {
        message: post 의 Text,
        name: post 의 like count,
        school: "학교"
    }
 */
}