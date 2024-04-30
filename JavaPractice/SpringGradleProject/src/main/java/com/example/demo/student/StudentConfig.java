package com.example.demo.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.util.List;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(StudentRepository repository) {
        return args -> {
            Student billy = new Student(
                    "Billy",
                    "example@gmail.com",
                    LocalDate.of(1990, 06, 9)
            );

            Student bob = new Student(
                    "Bob",
                    "example2@gmail.com",
                    LocalDate.of(1992, 02, 27)
            );

            repository.saveAll(
                    List.of(billy, bob)
            );
        };
    }
}
